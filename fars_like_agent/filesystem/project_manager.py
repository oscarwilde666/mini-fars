from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict


@dataclass
class ProjectManager:
    root: Path

    def create_project(self, project_id: str) -> Path:
        base = self.root / "projects" / project_id
        (base / "experiments" / "code").mkdir(parents=True, exist_ok=True)
        (base / "experiments" / "results").mkdir(parents=True, exist_ok=True)
        (base / "experiments" / "logs").mkdir(parents=True, exist_ok=True)
        (base / "paper").mkdir(parents=True, exist_ok=True)
        return base

    def save_json(self, project_dir: Path, relative_path: str, payload: Dict[str, Any]) -> Path:
        target = project_dir / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
        return target

    def save_text(self, project_dir: Path, relative_path: str, content: str) -> Path:
        target = project_dir / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)
        return target
