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

    def step(self, action: SkillForgeAction) -> SkillForgeObservation:  # type: ignore[override]
        self._state.step_count += 1



        return SkillForgeObservation(

        )

    @property
    def state(self) -> State:
        """
        Get the current environment state.

        Returns:
            Current State with episode_id and step_count
        """
        return self._state
