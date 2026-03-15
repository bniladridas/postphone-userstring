import re


_PATTERN = re.compile(
    r"^(?P<app>[^/\s()]+)/(?P<version>[^/\s()]+) \((?P<system>[^()\r\n]+)\)$"
)


def parse_user_agent(user_agent: str):
    """
    Parse a basic user-agent string.
    """

    match = _PATTERN.fullmatch(user_agent)
    if not match:
        return None

    return match.groupdict()
