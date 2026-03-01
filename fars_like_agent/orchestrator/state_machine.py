from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ProjectState(str, Enum):
    CREATED = "CREATED"
    IDEATION = "IDEATION"
    PLANNING = "PLANNING"
    EXPERIMENTING = "EXPERIMENTING"
    WRITING = "WRITING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


_VALID_TRANSITIONS = {
    ProjectState.CREATED: {ProjectState.IDEATION, ProjectState.FAILED},
    ProjectState.IDEATION: {ProjectState.PLANNING, ProjectState.FAILED},
    ProjectState.PLANNING: {ProjectState.EXPERIMENTING, ProjectState.FAILED},
    ProjectState.EXPERIMENTING: {ProjectState.WRITING, ProjectState.FAILED},
    ProjectState.WRITING: {ProjectState.COMPLETED, ProjectState.FAILED},
    ProjectState.COMPLETED: set(),
    ProjectState.FAILED: set(),
}


@dataclass
class StateMachine:
    state: ProjectState = ProjectState.CREATED

    def transition(self, next_state: ProjectState) -> None:
        if next_state not in _VALID_TRANSITIONS[self.state]:
            raise ValueError(f"Invalid transition: {self.state} -> {next_state}")
        self.state = next_state
