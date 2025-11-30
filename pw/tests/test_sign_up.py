from typing import Generator, Any

import uuid
import pytest
from playwright.sync_api import Page, expect

from pw.pages.sign_up_page import SignUpPage


@pytest.fixture(scope="function")
def sign_up_page(page: Page) -> Generator[SignUpPage, Any, None]:
    """Provide a ready SignUpPage. Navigate to app and open Sign Up via header link."""
    page_obj = SignUpPage(page)
    page_obj.goto()
    page_obj.click_sign_up()
    yield page_obj


def test_sign_up_success(sign_up_page: SignUpPage) -> None:
    email = f"test_automation_{uuid.uuid4().hex[:8]}@holistiplan.com"
    password = "TestPass123!"
    sign_up_page.sign_up(email, password)
    sign_up_page.expect_confirmation_email_sent(email)



def test_sign_up_password_mismatch(sign_up_page: SignUpPage) -> None:
    email = "test_automation_5@holistiplan.com"
    sign_up_page.fill_email(email)
    sign_up_page.fill_password("password1_different")
    sign_up_page.fill_password_confirm("different_password")
    sign_up_page.click_sign_up_button()
    sign_up_page.expect_passwords_mismatch()

