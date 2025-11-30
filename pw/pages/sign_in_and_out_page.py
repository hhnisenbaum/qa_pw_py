from __future__ import annotations

from pw.pages.header_component_page import HeaderComponentPage
from playwright.sync_api import expect
import os


class SignInPage(HeaderComponentPage):
    """Page object for the Sign In page/component.

    Provides small helpers that map to the Playwright locators you supplied.
    """

    EMAIL_FIELD_NAME = "Email*"
    PASSWORD_FIELD_NAME = "Password*"
    SUCCESS_TEMPLATE = "Successfully signed in as"
    ERROR_TEMPLATE = "The email address and/or password you specified are not correct."

    def click_email_field(self) -> None:
        """Click the email textbox to focus it."""
        self.page.get_by_role("textbox", name=self.EMAIL_FIELD_NAME).click()

    def fill_email(self, email: str) -> None:
        """Fill the email textbox (clicks first to focus)."""
        self.click_email_field()
        self.page.get_by_role("textbox", name=self.EMAIL_FIELD_NAME).fill(email)
        self.click_email_field()

    def click_password_field(self) -> None:
        """Click the password textbox to focus it."""
        self.page.get_by_role("textbox", name=self.PASSWORD_FIELD_NAME).click()

    def fill_password(self, password: str) -> None:
        """Fill the password textbox (no auto-click after fill)."""
        self.click_password_field()
        self.page.get_by_role("textbox", name=self.PASSWORD_FIELD_NAME).fill(password)

    def click_sign_in_button(self) -> None:
        """Click the 'Sign In' button."""
        self.page.get_by_role("button", name="Sign In").click(timeout=60000)

    def expect_successful_sign_in(self, email: str) -> None:
        """Assert the success message is present in the page body."""
        text = "Successfully signed in as {email}"
        expected = text.format(email=email)
        expect(self.page.get_by_text(self.SUCCESS_TEMPLATE)).to_contain_text(expected)

    def expect_error_on_sign_in(self) -> None:
        """Assert the error message is present in the page body."""
        expect(self.page.get_by_text(self.ERROR_TEMPLATE)).to_contain_text(
            "The email address and/or password you specified are not correct.")

    def sign_in(self, email: str, password: str | None = None) -> None:
        """Perform the full sign in flow and optionally assert success.

        If `password` is None, read `USER_PASSWORD` from environment.
        """
        if password is None:
            password = os.environ.get("USER_PASSWORD")
            if password is None:
                raise RuntimeError("No password provided and USER_PASSWORD not set in environment")

        self.fill_email(email)
        self.fill_password(password)
        self.click_sign_in_button()

