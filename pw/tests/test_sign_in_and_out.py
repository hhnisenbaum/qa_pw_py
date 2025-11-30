from typing import Generator, Any
import pytest
from playwright.sync_api import Page

from pw.pages.home_page import HomePage
from pw.pages.sign_in_and_out_page import SignInPage

TEST_EMAIL = "test_automation_1@holistiplan.com"

@pytest.fixture(scope="function")
def sign_in_page(page: Page) -> Generator[SignInPage, Any, None]:
    page_obj = SignInPage(page)
    page_obj.goto()
    page_obj.click_sign_in()
    yield page_obj

def test_sign_in_and_log_out(sign_in_page: SignInPage) -> None:
    sign_in_page.sign_in(TEST_EMAIL)
    sign_in_page.expect_successful_sign_in(TEST_EMAIL)
    sign_in_page.click_sign_out()
    sign_in_page.click_sign_out_button()
    home = HomePage(sign_in_page.page)
    home.expect_signed_out_message()

def test_sign_in_incorrect_password(sign_in_page: SignInPage) -> None:
    sign_in_page.sign_in(TEST_EMAIL, "fake_password123")
    sign_in_page.expect_error_on_sign_in()
