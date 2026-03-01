from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict

from ..agents import ExperimentAgent, IdeationAgent, PlanningAgent, WritingAgent
from ..filesystem import ProjectManager
from .state_machine import ProjectState, StateMachine


@dataclass
class WorkflowOrchestrator:
    workspace_root: Path
    ideation_agent: IdeationAgent = field(default_factory=IdeationAgent)
    planning_agent: PlanningAgent = field(default_factory=PlanningAgent)
    experiment_agent: ExperimentAgent = field(default_factory=ExperimentAgent)
    writing_agent: WritingAgent = field(default_factory=WritingAgent)

    def run_project(self, project_id: str, research_direction: str) -> Dict[str, Any]:
        sm = StateMachine()
        pm = ProjectManager(self.workspace_root)
        project_dir = pm.create_project(project_id)

        metadata: Dict[str, Any] = {
            "project_id": project_id,
            "research_direction": research_direction,
            "state": sm.state.value,
            "events": [],
        }

        try:
            sm.transition(ProjectState.IDEATION)
            ideation = self.ideation_agent.process({"research_direction": research_direction})
            pm.save_json(project_dir, "hypothesis.json", ideation)
            metadata["events"].append("hypothesis_generated")

            sm.transition(ProjectState.PLANNING)
            planning = self.planning_agent.process(ideation)
            pm.save_json(project_dir, "plan.json", planning)
            metadata["events"].append("plan_ready")

            sm.transition(ProjectState.EXPERIMENTING)
            experiment = self.experiment_agent.process(planning)
            pm.save_json(project_dir, "experiments/results/results.json", experiment)
            metadata["events"].append("experiment_completed")

            sm.transition(ProjectState.WRITING)
            writing_input = {**ideation, **planning, **experiment}
            paper = self.writing_agent.process(writing_input)
            pm.save_text(project_dir, "paper/draft.md", paper["paper"]["draft_markdown"])
            metadata["events"].append("paper_drafted")

            sm.transition(ProjectState.COMPLETED)
        except Exception as exc:  # pragma: no cover - defensive guard
            sm.transition(ProjectState.FAILED)
            metadata["error"] = str(exc)

        metadata["state"] = sm.state.value
        pm.save_json(project_dir, "metadata.json", metadata)

        return {
            "project_dir": str(project_dir),
            "state": metadata["state"],
            "events": metadata["events"],
        }
