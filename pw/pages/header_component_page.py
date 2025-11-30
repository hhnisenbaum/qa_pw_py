from typing import Optional

from pw.pages.base_page import BasePage
from playwright.sync_api import expect


class HeaderComponentPage(BasePage):
    """Reusable header component actions used across page objects."""

    def click_home_current(self) -> None:
        """Click the "Home (current)" header link."""
        self.click_link_by_name("Home (current)")

    def click_about(self) -> None:
        """Click the "About" header link."""
        self.click_link_by_name("About")

    def click_my_profile(self) -> None:
        """Click the "My Profile" header link."""
        self.click_link_by_name("My Profile")

    def click_sign_up(self) -> None:
        """Click the "Sign Up" header link."""
        self.click_link_by_name("Sign Up")

    def click_sign_in(self) -> None:
        """Click the "Sign In" header link using exact matching."""
        self.click_link_by_name("Sign In", exact=True)

    def click_sign_out(self) -> None:
        """Click the "Sign Out" header link using exact matching."""
        self.click_link_by_name("Sign Out", exact=True)

    def expect_link_visible(self, name: str, timeout: Optional[int] = None, exact: bool = False) -> None:
        """Generic: assert a header link with the given name is visible.

        name: visible link text to match (passed to Playwright `name`)
        timeout: optional per-call timeout in milliseconds
        exact: whether to use exact matching for the link text
        """
        locator = self.page.get_by_role("link", name=name, exact=exact)
        if timeout:
            expect(locator).to_be_visible(timeout=timeout)
        else:
            expect(locator).to_be_visible()

