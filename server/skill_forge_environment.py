# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

"""
Skill Forge Environment Implementation.

An RL training environment where LLM Agents evolve from "reinventing the wheel" to "building a skill library."
"""

from uuid import uuid4

from openenv.core.env_server.interfaces import Environment
from openenv.core.env_server.types import State

from models import SkillForgeAction, SkillForgeObservation
from data_generator import TASKS

class SkillForgeEnvironment(Environment):
    """
    A simple echo environment that echoes back messages.

    This environment is designed for testing the HTTP server infrastructure.
    It maintains minimal state and simply echoes back whatever message it receives.

    Example:
        >>> env = SkillForgeEnvironment()
        >>> obs = env.reset()
        >>> print(obs.echoed_message)  # "Skill Forge environment ready!"
        >>>
        >>> obs = env.step(SkillForgeAction(message="Hello"))
        >>> print(obs.echoed_message)  # "Hello"
        >>> print(obs.message_length)  # 5
    """

    # Enable concurrent WebSocket sessions.
    # Set to True if your environment isolates state between instances.
    # When True, multiple WebSocket clients can connect simultaneously, each
    # getting their own environment instance (when using factory mode in app.py).
    SUPPORTS_CONCURRENT_SESSIONS: bool = True

    def __init__(self):
        """Initialize the skill_forge environment."""
        self._state = State(episode_id=str(uuid4()), step_count=0)
        self._reset_count = 0

        self.skill_library = {}
        self.task_idx = 0
        self.action_history = []
        self.error_history = []

    def reset(self) -> SkillForgeObservation:
        """
        Reset the environment.
        skill_library intentionally NOT reset — persists across episodes

        Returns:
            SkillForgeObservation with a ready message
        """
        self._state = State(episode_id=str(uuid4()), step_count=0)
        self._reset_count += 1

        self.task_idx = 0
        task = TASKS[self.task_idx]
        self.action_history = []
        self.error_history = []

        return SkillForgeObservation(
            task_id=task["id"],
            task_description=task["description"],
            snapshot_data=task["dataframe"].head(5).to_string(),
            skill_library=self.current_state.skill_library,
            context="",
            step_count=0,
            total_tokens=0,
            result_correct=False,
            result_output="",
            expected_output=task["expected_output"],
        )

    def step(self, action: SkillForgeAction) -> SkillForgeObservation:  
        # TODO: create function _is_redundant
        self._state.step_count += 1

        if action.action_type not in ["create_skill", "use_skill", "raw_code"]:
            raise ValueError(f"Invalid action type: {action.action_type}")

        task = TASKS[self.task_idx]
        reward = 0.0
        
        if action.action_type == "create_skill":
            self.current_state.skill_library[action.skill_name] = {
                "template": action.content,
                "description": action.reasoning,
                "used_count": 0,
            }
            reward = 0.5 # TODO: revisit this value. Set it a bit high as we reward exploration 
            result_correct = False
            result_output = f"Skill {action.skill_name} created"
        else:
            if action.action_type == "use_skill":
                skill = self.current_state.skill_library.get(action.content)                
                # TODO: if action_type is use_skill while we don't have the skill yet, read reasoning to understand why the skill should be used and create the skill accordingly
                if skill: 
                    exec_code = skill["template"].format(**(action.params or {}))
                    self.current_state.skill_library[action.content]["used_count"] += 1
                else: # TODO: log this scenario
                    exec_code = None
            else:
                exec_code = action.code # TODO: add a penalty if we have a skill in skill lib for this problem

            # TODO: dataframe shouldn't be part of the task, the design is ugly
            result_correct, result_output = self._evaluate(exec_code, task["dataframe"], task["expected_output"])
            reward += 2.0 if result_correct else -1.0
            reward -= 0.001 * len(action.content)  # token penalty
            if action.action_type == "use_skill" and result_correct:
                reward += 0.5 # reward for using a skill that worked
            
            # TODO P0: update the context with action history and error history 

            # advance task
            self.task_idx = min(self.task_idx + 1, len(TASKS) - 1)
            done = self.task_idx == len(TASKS) - 1
            next_task = TASKS[self.task_idx]

        return SkillForgeObservation(
            task_id=next_task["id"],
            task_description=next_task["description"],
            snapshot_data=next_task["dataframe"].head(5).to_string(),
            skill_library=self.skill_library,
            context="",
            step_count=self._state.step_count,
            total_tokens=0, # TODO P0: update this with the total tokens used
            result_correct=result_correct,
            result_output=result_output,
            expected_output=next_task["expected_output"],
        )
    
    def _evaluate(self, exec_code, dataframe, expected_output):
        # TODO P0: implement this
        return True, "Evaluation successful"

    @property
    def state(self) -> State:
        """
        Get the current environment state.

        Returns:
            Current State with episode_id and step_count
        """
        return self._state
