**SkillForge** — An RL training environment where LLM Agents evolve from "reinventing the wheel" to "building a tool library."

## What It Is

An OpenEnv RL environment that trains an agent to **discover and reuse parameterized code skills** across a sequence of Python DataFrame tasks. The core thesis: an agent that builds a skill library solves the same set of tasks in fewer steps than one that generates from scratch every time.

## Core Concept

When solving DataFrame processing tasks, the Agent can choose:

1. **Raw Code**: Write full code from scratch every time (high token cost)
2. **Create Skill**: Abstract common operations (e.g., sort, filter) into reusable templates and save to Skill Library
3. **Use Skill**: Call stored skills (low token cost)

**Key Mechanism**: Skill Library **persists across Episodes**. Through training, the Agent discovers that reusing existing skills yields higher rewards than rewriting code.

## Key Features
- **Persistent Skill Library**: JSON-based storage that survives across episodes (simulates "learning to remember")
- **Redundancy Detector**: Penalizes agents for rewriting existing functionality
- **Token Accountant**: Tracks computational cost (simulated API expenses)
## Tech Stack (OpenEnv)

- **Environment**: `skill_forge` (modified from coding_env, executes Python/Pandas code)
- **Action Space**: `raw_code` | `create_skill` | `use_skill` | `finish`
- **Reward**: Task completion (sparse) + Token efficiency (dense) + Skill reuse rate (innovation)
- **Training**: GRPO (single-agent, stable convergence)
