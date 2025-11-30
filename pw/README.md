pytest-playwright tests

This directory is reserved for Playwright browser tests run via pytest and
`pytest-playwright`.

Quick start

1. Install dependencies

If you use pip/requirements, add `pytest-playwright` to your test dependencies. You can install locally with:

```bash
python -m pip install --upgrade pip
python -m pip install pytest-playwright
```

Note: `pytest-playwright` depends on the `playwright` package which provides the browser binaries installer command. After installing the package run the Playwright install step:

```bash
python -m playwright install
```

This will download browser engines used by tests (Chromium, Firefox, WebKit). For CI you should run the same `playwright install` step in your pipeline.

2. Run Playwright tests with pytest

Run all Playwright tests:

```bash
pytest tests/playwright -q
```

Run a single test file:

```bash
pytest tests/playwright/test_example_playwright.py -q
```

3. Example test

Place browser tests in this directory and use the `page` fixture provided by `pytest-playwright`:

```python
# tests/playwright/test_example_playwright.py

def test_basic_page_navigation(page):
    page.goto("https://example.com")
    assert "Example Domain" in page.title()
```

4. CI notes

- Ensure you run `python -m playwright install` (or `playwright install`) in CI before running tests so browser binaries are available.
- If running in a container, install required system dependencies for browsers or use the official Playwright Docker images.

5. Optional

If you'd like, I can add a small example test file (`test_example_playwright.py`) to this directory to help get started.
