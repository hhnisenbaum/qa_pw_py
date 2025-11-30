from __future__ import annotations

from playwright.sync_api import Page, expect
import os


class BasePage:
    """Base page object with shared utilities and configuration.

    Put common variables, navigation helpers and small utilities here so other
    page objects can inherit them.
    """

    def __init__(self, page: Page, base_url: str | None = None, base_timeout: int = 60000):
        self.page = page
        self.base_url = base_url or os.environ.get("BASE_URL") or "http://localhost:3000/"
        self.base_timeout = base_timeout

    def goto(self, path: str = "") -> None:
        """Navigate to a path on the application.

        If `path` is a full URL (starts with http), it will be opened as-is.
        Otherwise it will be joined with the configured `base_url`.
        """
        if path.startswith("http"):
            url = path
        else:
            url = self.base_url.rstrip("/") + "/" + path.lstrip("/")
        self.page.goto(url, timeout=self.base_timeout)
        self.click_hide_toolbar()


    def click_hide_toolbar(self) -> None:
        """Click the "Hide »" link."""
        expect(self.page.get_by_role("link", name="Hide »")).to_be_visible()
        self.page.get_by_role("link", name="Hide »").click()

    def get_test_id(self, test_id: str):
        """Shortcut to get an element by data-testid."""
        return self.page.get_by_test_id(test_id)

    def click_link_by_name(self, name: str, exact: bool = False) -> None:
        """Shortcut to click a link by role and name.

        `exact=True` will pass through to Playwright's exact matching.
        """
        self.page.get_by_role("link", name=name, exact=exact).click(timeout=self.base_timeout)

