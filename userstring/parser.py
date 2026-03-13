import re


pattern = r"(?P<app>.+)/(?P<version>.+) \((?P<system>.+)\)"


def parse_user_agent(user_agent: str):
    """
    Parse a basic user-agent string.
    """

    match = re.match(pattern, user_agent)
    if not match:
        return None

    return match.groupdict()
