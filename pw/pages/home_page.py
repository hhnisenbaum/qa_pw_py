from playwright.sync_api import Page, expect
from typing import Literal
from pw.pages.header_component_page import HeaderComponentPage

class HomePage(HeaderComponentPage):
    """Page Object Model for the application's home page.

    Extends HeaderComponentPage to reuse header link interactions.
    """

    def __init__(self, page: Page):
        super().__init__(page)

    def click_to_add_points(self, points: Literal[5, 15]) -> None:
        if points not in (5, 15):
            raise ValueError("points must be either 5 or 15")
        link_name = f"+{points}"
        link = self.page.get_by_role("link", name=link_name)
        link.wait_for(state="visible", timeout=self.base_timeout)
        link.click(force=True)

    def click_forfeit_all_points(self) -> None:
        self.page.get_by_role("link", name="forfeit all points").click()

    def expect_points_remaining_to_contain(self, text: str) -> None:
        expect(self.page.get_by_test_id("points-remaining")).to_contain_text(text,timeout=self.base_timeout)

    def expect_points_redeemed_to_contain(self, text: str) -> None:
        expect(self.page.get_by_test_id("points-redeemed")).to_contain_text(text,timeout=self.base_timeout)

    def expect_signed_out_message(self) -> None:
        expect(self.page.get_by_text("You have signed out.")).to_contain_text("You have signed out.")
