from .constants import DEFAULT_APP, DEFAULT_SYSTEM, DEFAULT_VERSION


def build_user_agent(app=DEFAULT_APP, version=DEFAULT_VERSION, system=DEFAULT_SYSTEM):
    """
    Build a simple user-agent string.
    """

    return f"{app}/{version} ({system})"
