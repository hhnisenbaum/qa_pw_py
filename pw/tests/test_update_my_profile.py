from typing import Generator, Optional, Tuple

import pytest
from playwright.sync_api import Page

from pw.pages.my_profile_page import MyProfilePage
from pw.pages.sign_in_and_out_page import SignInPage


@pytest.fixture(scope="function")
def signed_in_profile(page: Page, request) -> Generator[tuple[MyProfilePage, Optional[str]], None, None]:
    email = getattr(request, "param", None)
    signin = SignInPage(page)
    signin.goto()
    signin.click_sign_in()
    if email:
        signin.sign_in(email)

    my_profile = MyProfilePage(page)
    yield my_profile, email


@pytest.mark.parametrize("signed_in_profile", ["test_automation_2@holistiplan.com"], indirect=True)
def test_update_my_user_name_profile(signed_in_profile: Tuple[MyProfilePage, Optional[str]]) -> None:
    my_profile_page, email = signed_in_profile
    my_profile_page.update_name(email)
    my_profile_page.expect_user_name_to_be(email)
    my_profile_page.expect_successful_user_name_update_message()


@pytest.mark.parametrize("signed_in_profile", ["test_automation_3@holistiplan.com"], indirect=True)
def test_make_my_primary_email(signed_in_profile: Tuple[MyProfilePage, Optional[str]]) -> None:
    my_profile_page, email = signed_in_profile
    my_profile_page.make_email_primary()
    my_profile_page.expect_primary_email_set()
