from importlib.metadata import PackageNotFoundError, version as pkg_version


DEFAULT_SYSTEM = "unknown"
DEFAULT_APP = "userstring"


def _default_version() -> str:
    try:
        return pkg_version("userstring")
    except PackageNotFoundError:
        return "0.1.0"


DEFAULT_VERSION = _default_version()
