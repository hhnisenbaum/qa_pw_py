from playwright.sync_api import Page, expect
from pw.pages.home_page import HomePage


def test_add_15_points(page: Page) -> None:
    home = HomePage(page)
    home.goto()
    expect(page.get_by_role("link", name="Hide »")).to_be_visible()
    home.click_hide()
    home.click_forfeit_all_points()
    home.click_add_15()
    home.expect_points_remaining_to_contain("15")

def test_add_5_points(page: Page) -> None:
    home = HomePage(page)
    home.goto()
    expect(page.get_by_role("link", name="Hide »")).to_be_visible()
    home.click_hide()
    home.click_forfeit_all_points()
    home.click_add_15()
    home.expect_points_remaining_to_contain("5")
