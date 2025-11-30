from typing import Generator, Any
import pytest
from playwright.sync_api import Page
from pw.pages.password_reset_page import PasswordResetPage
from pw.pages.sign_in_and_out_page import SignInPage

@pytest.fixture(scope="function")
def password_reset_page(page: Page) -> Generator[PasswordResetPage, Any, None]:
    sign_in_page = SignInPage(page)
    sign_in_page.goto()
    sign_in_page.click_sign_in()
    sign_in_page.click_link_forgot_your_password()
    page_obj = PasswordResetPage(page)
    yield page_obj

def test_reset_password_successfully(password_reset_page: PasswordResetPage) -> None:
    password_reset_page.reset_password("fakeemail@fakeemail.com")
    password_reset_page.expect_email_sent()
