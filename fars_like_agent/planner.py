from __future__ import annotations

from .models import Action, Plan


class HeuristicPlanner:
    def build_plan(self, goal: str) -> Plan:
        actions = []
        if any(ch.isdigit() for ch in goal) and any(op in goal for op in ["+", "-", "*", "/"]):
            actions.append(
                Action(
                    tool="calculator",
                    input=goal,
                    rationale="Goal appears to include a math expression.",
                )
            )
        else:
            actions.append(
                Action(
                    tool="echo",
                    input=goal,
                    rationale="No specialized tool inferred; gather baseline context.",
                )
            )
        return Plan(goal=goal, actions=actions)

