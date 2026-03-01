from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from .models import Evidence


@dataclass
class MemoryStore:
    items: List[Evidence] = field(default_factory=list)

    def add(self, evidence: Evidence) -> None:
        self.items.append(evidence)

    def retrieve(self, query: str, top_k: int = 3) -> List[Evidence]:
        query_tokens = {t.lower() for t in query.split()}

        def score(item: Evidence) -> int:
            content_tokens = {t.lower() for t in item.content.split()}
            return len(query_tokens.intersection(content_tokens))

        ranked = sorted(self.items, key=score, reverse=True)
        return [x for x in ranked[:top_k] if score(x) > 0]

