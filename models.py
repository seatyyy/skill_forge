# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

"""
Data models for the Skill Forge Environment.

The skill_forge environment is a simple test environment that echoes back messages.
"""

from pydantic import Field, BaseModel
from typing import Literal, Optional, Dict, List

from openenv.core.env_server.types import Action, Observation

class SkillForgeAction(Action):
    """Action for the Skill Forge environment"""
    action_type: Literal["create_skill", "use_skill", "raw_code"]
    content: str = Field(description="The content of the action. For create_skill, it is the template. For use_skill, it is the skill id. For raw_code, it is the code.")
    skill_name: Optional[str] # only for create_skill
    reasoning: str = ""
    params: Optional[dict] = None


class SkillForgeObservation(Observation):
    """Observation from the Skill Forge environment."""
    task_id: str
    task_description: str
    snapshot_data: str  #df.head(5).to_string()
    skill_library: List[Dict]
    context: str 
    result_correct: bool
    result_output: str
    expected_output: str
    step_count: int
    total_tokens: int

