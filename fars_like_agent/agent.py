from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from .memory import MemoryStore
from .models import AgentResponse, Evidence, Observation
from .planner import HeuristicPlanner
from .tools import ToolRegistry, default_registry


@dataclass
class FARSLikeAgent:
    planner: HeuristicPlanner = field(default_factory=HeuristicPlanner)
    tools: ToolRegistry = field(default_factory=default_registry)
    memory: MemoryStore = field(default_factory=MemoryStore)

    def run(self, goal: str) -> AgentResponse:
        trace: List[str] = []

        plan = self.planner.build_plan(goal)
        trace.append(f"PLAN: {len(plan.actions)} action(s)")

        observations: List[Observation] = []
        for idx, action in enumerate(plan.actions, start=1):
            trace.append(f"ACT {idx}: {action.tool}({action.input!r})")
            try:
                output = self.tools.run(action.tool, action.input)
                obs = Observation(tool=action.tool, output=output, ok=True)
            except Exception as exc:
                obs = Observation(tool=action.tool, output="", ok=False, error=str(exc))
            observations.append(obs)
            trace.append(f"OBS {idx}: ok={obs.ok} output={obs.output!r} error={obs.error!r}")

        evidence: List[Evidence] = []
        for obs in observations:
            if obs.ok:
                ev = Evidence(source=f"tool:{obs.tool}", content=obs.output)
                evidence.append(ev)
                self.memory.add(ev)

        memory_hits = self.memory.retrieve(goal, top_k=2)
        if memory_hits:
            trace.append(f"GROUND: {len(memory_hits)} memory hit(s)")
            evidence.extend(memory_hits)

        if evidence:
            answer = f"基于证据，任务结果如下：{evidence[0].content}"
        else:
            answer = "无法获得可靠证据，请补充更具体的问题或接入外部工具。"

        return AgentResponse(answer=answer, evidence=evidence, trace=trace)

