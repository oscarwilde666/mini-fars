from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from .base_agent import BaseAgent


@dataclass
class PlanningAgent(BaseAgent):
    name: str = "planning"

    def process(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        statement = payload["hypothesis"]["statement"]
        plan = {
            "hypothesis_statement": statement,
            "steps": [
                "收集近两年相关文献并标注研究空白",
                "定义基线系统与评测集",
                "实现带证据引用的 agent 回答流程",
                "运行对比实验并统计可靠性指标",
            ],
            "resources": {"gpu_hours": 2, "storage_gb": 5},
            "metrics": ["citation_coverage", "answer_faithfulness", "task_success_rate"],
        }
        return {"plan": plan}
