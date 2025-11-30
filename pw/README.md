# pw — Playwright + pytest UI tests

This directory contains Playwright-based page objects and pytest tests used for end-to-end UI testing.

This README explains how to set up a development environment from scratch, install required dependencies (Python and Playwright), and run the tests.

---

## Prerequisites

- Python 3.10+ (project `pyproject.toml` targets 3.11 but 3.10+ works)
- pip (Python package installer)
- Git (optional)

Optional (only if you use Playwright Node tools):
- Node.js and npm

---

## Quick setup (recommended)

1. Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install Python dependencies used by the `pw` tests. The repo keeps test deps in `requirements/local.txt` — install them all:

```bash
pip install -r requirements/local.txt
#This packages were added to local pytest pytest-playwright pytest-xdist
```

3. Install Playwright browser binaries (required once per machine / CI runner):

```bash
python -m playwright install
# for full dependencies (Linux CI) you can run:
# python -m playwright install --with-deps
```

4. (Optional) If the repository contains a `pw/.env` file with environment variables, the test suite loads it automatically — otherwise set env vars manually if needed.

Common variables you may set in `pw/.env` or your shell:
- `BASE_URL` — base URL of the web app under test (default: http://localhost:3000/)
- `USER_PASSWORD` — default password used by sign-in helpers

---

## Running tests

Run tests from the repository root.

- Run the entire test suite for the `pw` folder:

```bash
pytest pw/tests -q
```

- Run a single test by node id (preferred):

```bash
pytest pw/tests/test_sign_up.py::test_sign_up_password_mismatch -q
```

- Run tests using a specific browser (pytest-playwright):

```bash
pytest --browser=chromium pw/tests -q
pytest --browser=firefox pw/tests -q
pytest --browser=webkit pw/tests -q
```

- Show verbose output and prints (useful while debugging):

```bash
pytest pw/tests -s -q
```

---

## pytest.ini (pw/pytest.ini)

The `pw/pytest.ini` file controls pytest behavior for tests inside the `pw/` directory. Use it to set defaults that only apply when you run pytest from `pw/` (or when pytest discovers tests under that folder).

Common uses:

- Set `addopts` to add default CLI flags (for example, run tests in parallel and pick a default browser).
- Configure the test discovery pattern with `python_files`.
- Keep `addopts` empty if you want to avoid global project-level options being applied to these tests.

Example `pw/pytest.ini` you can use or adapt:

```ini
[pytest]
# run tests with xdist using 2 workers and default to Chromium
addopts = -n 2 --browser=chromium
python_files = test_*.py
```



## Project layout (relevant)

- `pw/pages/` — Page Object Models (POMs) wrapping Playwright interactions
- `pw/tests/` — pytest files exercising the UI
- `pw/conftest.py` — fixtures (the test suite auto-loads `pw/.env` if present)
- `pw/pytest.ini` — pytest config for tests in this folder
