from userstring.constants import DEFAULT_APP, DEFAULT_SYSTEM, DEFAULT_VERSION
from userstring.generator import build_user_agent


def test_user_agent():
    ua = build_user_agent("testapp", "1.0", "linux")
    assert ua == "testapp/1.0 (linux)"


def test_user_agent_defaults():
    ua = build_user_agent()
    assert ua == f"{DEFAULT_APP}/{DEFAULT_VERSION} ({DEFAULT_SYSTEM})"
