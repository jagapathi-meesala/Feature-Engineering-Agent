import os


def get_setting(name: str, *, required: bool = False, default: str | None = None) -> str | None:
    value = os.getenv(name)
    if value is None or value == "":
        if required:
            raise RuntimeError(f"Required environment variable is missing: {name}")
        return default
    return value


ENVIRONMENT = get_setting("ENVIRONMENT", required=True)
LOG_LEVEL = get_setting("LOG_LEVEL", required=True)
MAX_ROWS = int(get_setting("MAX_ROWS", required=True))
MAX_COLUMNS = int(get_setting("MAX_COLUMNS", required=True))
