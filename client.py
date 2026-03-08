# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

"""Skill Forge Environment Client."""

from typing import Dict

from openenv.core.client_types import StepResult
from openenv.core.env_server.types import State
from openenv.core import EnvClient

from .models import SkillForgeAction, SkillForgeObservation


class SkillForgeEnv(
    EnvClient[SkillForgeAction, SkillForgeObservation, State]
):
    """
    Client for the Skill Forge Environment.

    Maintains a persistent WebSocket connection to the environment server.
    Each client instance has its own dedicated environment session.

    Example:
        >>> with SkillForgeEnv(base_url="http://localhost:8000") as client:
        ...     result = client.reset()
        ...     print(result.observation.task_description)
        ...
        ...     action = SkillForgeAction(
        ...         action_type="raw_code",
        ...         content="df.sort_values('revenue', ascending=False)['product'].tolist()",
        ...     )
        ...     result = client.step(action)
        ...     print(result.observation.result_correct)
    """

    def _step_payload(self, action: SkillForgeAction) -> Dict:
        return action.model_dump()

    def _parse_result(self, payload: Dict) -> StepResult[SkillForgeObservation]:
        obs_data = payload.get("observation", {})
        observation = SkillForgeObservation(**obs_data)

        return StepResult(
            observation=observation,
            reward=payload.get("reward"),
            done=payload.get("done", False),
        )

    def _parse_state(self, payload: Dict) -> State:
        return State(
            episode_id=payload.get("episode_id"),
            step_count=payload.get("step_count", 0),
        )
