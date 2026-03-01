from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from .base_agent import BaseAgent


@dataclass
class ExperimentAgent(BaseAgent):
    name: str = "experiment"

    def process(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        plan = payload["plan"]
        step_count = len(plan.get("steps", []))
        results = {
            "summary": "实验完成（模拟执行）。",
            "runs": [
                {"name": "baseline", "citation_coverage": 0.45, "faithfulness": 0.52},
                {"name": "fars_like", "citation_coverage": 0.81, "faithfulness": 0.76},
            ],
            "observations": [
                "带证据输出后，引用覆盖率显著提升。",
                "回答忠实度在复杂问题上仍有优化空间。",
            ],
            "executed_steps": step_count,
        }
        return {"results": results}
