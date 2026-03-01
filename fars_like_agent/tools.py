from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict


ToolFunc = Callable[[str], str]


@dataclass
class ToolRegistry:
    tools: Dict[str, ToolFunc]

    def run(self, name: str, tool_input: str) -> str:
        if name not in self.tools:
            raise ValueError(f"Unknown tool: {name}")
        return self.tools[name](tool_input)


def safe_calculator(expr: str) -> str:
    allowed = set("0123456789+-*/(). ")
    if any(ch not in allowed for ch in expr):
        raise ValueError("calculator only allows numeric expressions")
    return str(eval(expr, {"__builtins__": {}}, {}))


def echo(text: str) -> str:
    return text


def default_registry() -> ToolRegistry:
    return ToolRegistry(
        tools={
            "calculator": safe_calculator,
            "echo": echo,
        }
    )

