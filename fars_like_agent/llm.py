from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LLMClient:
    """Placeholder LLM interface.

    Replace `complete` with actual provider calls (OpenAI/Anthropic/local model).
    """

    model: str = "heuristic"

    def complete(self, prompt: str) -> str:
        return f"[heuristic:{self.model}] {prompt[:120]}"

