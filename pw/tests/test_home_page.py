import pytest
from playwright.sync_api import Page, expect
from pw.pages.home_page import HomePage


@pytest.fixture(scope="function")
def home(page: Page):
    """Setup the HomePage and return it to the test.
    """
    home = HomePage(page)
    home.goto()
    home.click_forfeit_all_points()
    home.expect_points_remaining_to_contain("0")
    yield home


def test_add_15_points(home: HomePage) -> None:
    home.click_to_add_points(15)
    home.expect_points_remaining_to_contain("15")


def test_add_5_points(home: HomePage) -> None:
    home.click_to_add_points(5)
    home.expect_points_remaining_to_contain("5")
