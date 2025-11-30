from playwright.sync_api import expect

from pw.pages.header_component_page import HeaderComponentPage


class MyProfilePage(HeaderComponentPage):
    """Page object for the My Profile page/component.

    Provides helpers for interacting with the "My Info" section of the header
    and updating the user's name.
    """

    NAME_FIELD = "Name of User"
    SUCCESS_MESSAGE = "Information successfully updated"
    PRIMARY_EMAIL_SUCCESS_MESSAGE = "Primary email address set."

    def click_my_info(self) -> None:
        """Click the "My Info" button to open the profile/edit view."""
        self.page.get_by_role("button", name="My Info").click(timeout=self.base_timeout)

    def fill_name_of_user(self, name: str) -> None:
        """Fill the Name of User textbox with `name`."""
        self.page.get_by_role("textbox", name=self.NAME_FIELD).fill(name)

    def click_update(self) -> None:
        """Click the Update button to save profile changes."""
        self.page.get_by_role("button", name="Update").click(timeout=self.base_timeout)

    def update_name(self, name: str) -> None:
        """Convenience method: open My Info, set the name and update."""
        self.click_my_info()
        self.fill_name_of_user(name)
        self.click_update()

    def expect_user_name_to_be(self, text: str) -> None:
        expect(self.page.get_by_role("heading", name=text)).to_contain_text(text)

    def expect_successful_user_name_update_message(self) -> None:
        expect(self.page.get_by_text(self.SUCCESS_MESSAGE)).to_contain_text(self.SUCCESS_MESSAGE)


    def click_email_section(self) -> None:
        """Open the E-Mail section of the profile."""
        self.page.get_by_role("button", name="E-Mail").click(timeout=self.base_timeout)

    def click_make_primary(self) -> None:
        """Click the 'Make Primary' button for the selected email."""
        self.page.get_by_role("button", name="Make Primary").click(timeout=self.base_timeout)

    def expect_primary_email_set(self) -> None:
        """Assert the primary email success message is shown."""
        expect(self.page.get_by_text(self.PRIMARY_EMAIL_SUCCESS_MESSAGE)).to_contain_text(
            self.PRIMARY_EMAIL_SUCCESS_MESSAGE
        )

    def make_email_primary(self) -> None:
        """Convenience flow: open email section, make primary and assert success."""
        self.click_email_section()
        self.click_make_primary()
