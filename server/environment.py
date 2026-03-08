# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

"""
Skill Forge Environment Implementation.

An RL training environment where LLM Agents evolve from "reinventing the wheel" to "building a skill library."
"""

import json
import traceback
from uuid import uuid4

import pandas as pd

from openenv.core.env_server.interfaces import Environment
from openenv.core.env_server.types import State

try:
    from ..models import SkillForgeAction, SkillForgeObservation
    from .data_generator import TASKS
except ImportError:
    from models import SkillForgeAction, SkillForgeObservation
    from data_generator import TASKS


class SkillForgeEnvironment(Environment):
    """
    SkillForge RL environment.

    The agent solves chained pandas tasks and can build a reusable skill library.
    Skills persist across episodes so the agent can discover and reuse patterns.
    """

    SUPPORTS_CONCURRENT_SESSIONS: bool = True

    def __init__(self):
        self._state = State(episode_id=str(uuid4()), step_count=0)
        self.skill_library: dict = {}
        self.task_idx: int = 0
        self.tasks_solved: int = 0
        self.total_tokens: int = 0

    def reset(self) -> SkillForgeObservation:
        """
        Reset episode state. skill_library is NOT reset — persists across episodes.
        """
        self._state = State(episode_id=str(uuid4()), step_count=0)
        self.task_idx = 0
        self.tasks_solved = 0
        self.total_tokens = 0

        task = TASKS[self.task_idx]
        return self._make_observation(task, result_correct=False, result_output="", reward=0.0, done=False)

    def step(self, action: SkillForgeAction) -> SkillForgeObservation:
        self._state.step_count += 1
        task = TASKS[self.task_idx]

        # --- create_skill: store template, stay on current task ---
        if action.action_type == "create_skill":
            token_cost = len(action.content)
            self.total_tokens += token_cost

            self.skill_library[action.skill_name] = {
                "template": action.content,
                "description": action.reasoning,
                "used_count": 0,
            }
            reward = 0.5
            return self._make_observation(
                task, result_correct=False,
                result_output=f"Skill '{action.skill_name}' saved.",
                reward=reward, done=False,
            )

        # --- use_skill or raw_code: execute and evaluate ---
        if action.action_type == "use_skill":
            skill = self.skill_library.get(action.content)
            if skill is None:
                # skill not found — treat as error
                self.total_tokens += len(action.content)
                return self._make_observation(
                    task, result_correct=False,
                    result_output=f"Skill '{action.content}' not found in library.",
                    reward=-0.3, done=False,
                )
            exec_code = skill["template"].format(**(action.params or {}))
            skill["used_count"] += 1
            # token cost for use_skill: skill name + serialized params (much shorter than full code)
            skill_call_repr = action.content + json.dumps(action.params or {})
            token_cost = len(skill_call_repr)
        else:
            # raw_code
            exec_code = action.content
            token_cost = len(action.content)

        self.total_tokens += token_cost

        result_correct, result_output = self._evaluate(exec_code, task["dataframe"], task["expected_output"])

        if result_correct:
            reward = 2.0
            reward -= 0.001 * token_cost
            if action.action_type == "use_skill":
                reward += 0.5
            self.tasks_solved += 1
            self.task_idx += 1
        else:
            reward = -0.3

        done = self.task_idx >= len(TASKS)
        next_task = TASKS[self.task_idx] if not done else task

        return self._make_observation(
            next_task,
            result_correct=result_correct,
            result_output=result_output,
            reward=reward,
            done=done,
        )

    def _evaluate(self, exec_code: str | None, dataframe: pd.DataFrame, expected_output) -> tuple[bool, str]:
        if exec_code is None:
            return False, "No code to execute."
        try:
            namespace = {"df": dataframe.copy(), "pd": pd, "__builtins__": {"len": len, "str": str, "int": int, "float": float, "list": list, "dict": dict, "bool": bool, "range": range, "abs": abs, "min": min, "max": max, "sum": sum, "sorted": sorted, "round": round, "True": True, "False": False, "None": None}}
            result = eval(exec_code, namespace)

            # normalize for comparison
            if isinstance(result, pd.DataFrame):
                result = result.values.tolist()
            if isinstance(result, pd.Series):
                result = result.tolist()
            if isinstance(result, pd.Index):
                result = result.tolist()

            expected = expected_output
            if isinstance(expected, pd.Series):
                expected = expected.tolist()

            try:
                is_correct = result == expected
            except (ValueError, TypeError):
                is_correct = False

            return bool(is_correct), str(result)
        except Exception:
            return False, traceback.format_exc()

    def _make_observation(self, task: dict, result_correct: bool, result_output: str,
                          reward: float, done: bool) -> SkillForgeObservation:
        return SkillForgeObservation(
            task_id=task["id"],
            task_description=task["description"],
            snapshot_data=task["dataframe"].head(5).to_string(),
            skill_library=self.skill_library,
            context="",
            step_count=self._state.step_count,
            total_tokens=self.total_tokens,
            result_correct=result_correct,
            result_output=result_output,
            expected_output=str(task["expected_output"]),
            reward=reward,
            done=done,
        )

    @property
    def state(self) -> State:
        return self._state
