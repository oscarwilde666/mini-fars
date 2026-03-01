from __future__ import annotations

import argparse
import json
from pathlib import Path

from .orchestrator import WorkflowOrchestrator


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the new FARS-like 4-agent automated research workflow"
    )
    parser.add_argument("research_direction", help="Research topic/direction")
    parser.add_argument("--project-id", default="project_001", help="Project identifier")
    parser.add_argument("--workspace", default="workspace", help="Workspace root directory")
    args = parser.parse_args()

    orchestrator = WorkflowOrchestrator(workspace_root=Path(args.workspace))
    result = orchestrator.run_project(
        project_id=args.project_id,
        research_direction=args.research_direction,
    )

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
