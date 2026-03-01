from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from .base_agent import BaseAgent


@dataclass
class WritingAgent(BaseAgent):
    name: str = "writing"

    def process(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        hypothesis = payload["hypothesis"]["statement"]
        observations = payload["results"]["observations"]
        draft = "\n".join(
            [
                "# Draft Paper",
                "",
                "## Abstract",
                "本研究实现了一个 FARS-like 自动化研究流程骨架，并验证证据绑定对回答可靠性的提升。",
                "",
                "## Hypothesis",
                hypothesis,
                "",
                "## Key Findings",
                *[f"- {item}" for item in observations],
                "",
                "## Limitations",
                "当前实验阶段为模拟执行，后续应接入真实检索与训练任务。",
            ]
        )
        return {"paper": {"draft_markdown": draft}}
