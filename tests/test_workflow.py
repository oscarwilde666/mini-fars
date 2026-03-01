import json
from pathlib import Path

from fars_like_agent.orchestrator import WorkflowOrchestrator


def test_workflow_generates_expected_artifacts(tmp_path: Path):
    orchestrator = WorkflowOrchestrator(workspace_root=tmp_path)
    result = orchestrator.run_project("project_123", "RAG + self-check")

    project_dir = tmp_path / "projects" / "project_123"
    assert result["state"] == "COMPLETED"
    assert (project_dir / "hypothesis.json").exists()
    assert (project_dir / "plan.json").exists()
    assert (project_dir / "experiments" / "results" / "results.json").exists()
    assert (project_dir / "paper" / "draft.md").exists()

    metadata = json.loads((project_dir / "metadata.json").read_text())
    assert metadata["state"] == "COMPLETED"
    assert metadata["events"] == [
        "hypothesis_generated",
        "plan_ready",
        "experiment_completed",
        "paper_drafted",
    ]
