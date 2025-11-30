import os
from pathlib import Path
import pytest


def _load_dotenv(dotenv_path: Path) -> None:
    """Load simple KEY=VALUE pairs from a .env file into os.environ.

    This is a lightweight replacement for python-dotenv so tests can read
    `pw/.env` without adding a new dependency. Existing environment
    variables are not overridden.
    """
    if not dotenv_path.exists():
        return

    for line in dotenv_path.read_text(encoding="utf8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, val = line.split("=", 1)
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        # don't override already-set environment variables
        os.environ.setdefault(key, val)


@pytest.fixture(scope="session", autouse=True)
def load_pw_dotenv():
    """Automatically load pw/.env for tests under the `pw` package.

    This fixture runs once per test session and makes values like
    USER_PASSWORD and BASE_URL available in os.environ.
    """
    dotenv = Path(__file__).resolve().parent / ".env"
    _load_dotenv(dotenv)
    yield

