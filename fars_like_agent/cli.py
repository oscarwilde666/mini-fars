from __future__ import annotations

import argparse
import json

from .agent import FARSLikeAgent


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a minimal FARS-like agent")
    parser.add_argument("goal", help="Task or question for the agent")
    args = parser.parse_args()

    agent = FARSLikeAgent()
    result = agent.run(args.goal)
    print(
        json.dumps(
            {
                "answer": result.answer,
                "evidence": [e.__dict__ for e in result.evidence],
                "trace": result.trace,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

