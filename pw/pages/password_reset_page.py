from playwright.sync_api import expect
from pw.pages.base_page import BasePage

class PasswordResetPage(BasePage):
    """Page object for the password reset page/component."""

    EMAIL_FIELD = "Email*"
    RESET_BUTTON = "Reset My Password"
    SUCCESS_TEXT = "We have sent you an e-mail. Please contact us if you do not receive it within a few minutes."

    def fill_email(self, email: str) -> None:
        """Fill the email textbox."""
        self.page.get_by_role("textbox", name=self.EMAIL_FIELD).fill(email)

    def click_reset(self) -> None:
        """Click the Reset My Password button."""
        self.page.get_by_role("button", name=self.RESET_BUTTON).click(timeout=self.base_timeout)

    def expect_email_sent(self) -> None:
        expect(self.page.get_by_text(self.SUCCESS_TEXT)).to_contain_text(self.SUCCESS_TEXT, timeout=self.base_timeout)


    def reset_password(self, email: str) -> None:
        self.fill_email(email)
        self.click_reset()


