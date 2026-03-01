from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class Evidence:
    source: str
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Action:
    tool: str
    input: str
    rationale: str


@dataclass
class Plan:
    goal: str
    actions: List[Action]


@dataclass
class Observation:
    tool: str
    output: str
    ok: bool = True
    error: Optional[str] = None


@dataclass
class AgentResponse:
    answer: str
    evidence: List[Evidence]
    trace: List[str]

