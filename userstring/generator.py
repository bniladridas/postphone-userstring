import re

from .constants import DEFAULT_APP, DEFAULT_SYSTEM, DEFAULT_VERSION


_SAFE_COMPONENT = re.compile(r"^[A-Za-z0-9][A-Za-z0-9 ._\-+]*$")
_CONTROL_PATTERN = re.compile(r"[\r\n]")
_REPLACEMENTS = str.maketrans({"/": "-", "(": "[", ")": "]"})


def _sanitize_component(value: str, name: str) -> str:
    if value is None:
        raise ValueError(f"{name} must not be None")
    if not isinstance(value, str):
        value = str(value)

    if _CONTROL_PATTERN.search(value):
        raise ValueError(f"{name} must not contain CR or LF characters")

    sanitized = value.translate(_REPLACEMENTS).strip()
    if not sanitized:
        raise ValueError(f"{name} must not be empty after sanitization")

    if not _SAFE_COMPONENT.fullmatch(sanitized):
        raise ValueError(f"{name} contains unsafe characters")

    return sanitized


def build_user_agent(app=DEFAULT_APP, version=DEFAULT_VERSION, system=DEFAULT_SYSTEM):
    """
    Build a simple user-agent string with sanitized components.
    """

    app = _sanitize_component(app, "app")
    version = _sanitize_component(version, "version")
    system = _sanitize_component(system, "system")

    return f"{app}/{version} ({system})"
