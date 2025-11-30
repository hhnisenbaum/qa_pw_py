import re
from playwright.sync_api import Page, expect


class HomePage:
    """Page Object Model for the application's home page.

    This class wraps interactions with the page using the same locators you
    provided (role=link, name="Hide »" and name="+15").
    """

    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str = "http://localhost:3000/") -> None:
        """Navigate to the home page."""
        self.page.goto(url)

    def click_hide(self) -> None:
        """Click the "Hide »" link."""
        self.page.get_by_role("link", name="Hide »").click()

    def click_add_15(self) -> None:
        """Click the "+15" link."""
        self.page.get_by_role("link", name="+15").click()

