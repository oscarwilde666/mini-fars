from fars_like_agent.agent import FARSLikeAgent


def test_math_goal_uses_calculator():
    agent = FARSLikeAgent()
    result = agent.run("2+3*4")
    assert "14" in result.answer
    assert any(e.source == "tool:calculator" for e in result.evidence)


def test_text_goal_uses_echo():
    agent = FARSLikeAgent()
    result = agent.run("hello world")
    assert "hello world" in result.answer
    assert any(e.source == "tool:echo" for e in result.evidence)

