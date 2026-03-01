from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class BaseAgent(ABC):
    name: str

    def initialize(self) -> None:
        return None

    @abstractmethod
    def process(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError

    def validate(self, output: Dict[str, Any]) -> bool:
        return bool(output)
