
from playwright.sync_api import expect

from pw.pages.header_component_page import HeaderComponentPage


class SignUpPage(HeaderComponentPage):
    """Page object for the Sign Up page/component.
    """

    EMAIL_FIELD = "Email*"
    PASSWORD_FIELD = "Password*"
    PASSWORD_CONFIRM_FIELD = "Password (again)*"
    SIGNUP_BUTTON = "Sign Up »"
    ERROR_PASSWORD_MISSMATCH = "You must type the same password each time."
    SUCCESS_TEMPLATE = "Confirmation email sent to"

    def fill_email(self, email: str) -> None:
        self.page.get_by_role("textbox", name=self.EMAIL_FIELD).fill(email)

    def fill_password(self, password: str) -> None:
        self.page.get_by_role("textbox", name=self.PASSWORD_FIELD).fill(password)

    def fill_password_confirm(self, password: str) -> None:
        self.page.get_by_role("textbox", name=self.PASSWORD_CONFIRM_FIELD).fill(password)

    def click_sign_up_button(self) -> None:
        self.page.get_by_role("button", name=self.SIGNUP_BUTTON).click(timeout=self.base_timeout)

    def sign_up(self, email: str, password: str) -> None:
        self.fill_email(email)
        self.fill_password(password)
        self.fill_password_confirm(password)
        self.click_sign_up_button()

    def expect_passwords_mismatch(self) -> None:
        expect(self.page.get_by_text(self.ERROR_PASSWORD_MISSMATCH)).to_contain_text(self.ERROR_PASSWORD_MISSMATCH)

    def expect_confirmation_email_sent(self, email: str) -> None:
        text = "Confirmation email sent to {email}"
        expected = text.format(email=email)
        expect(self.page.get_by_text(self.SUCCESS_TEMPLATE)).to_contain_text(expected)


