import pytest
import logging
from login_main_page import Login_page_main
from playwright.sync_api import Playwright, TimeoutError as PlaywrightTimeoutError
from logger import get_logger

logging.basicConfig(level=logging.INFO)
logger = get_logger()

PASSWORD = '123456'
USER_EMAIL = 'TestUser@gmail.com'
TIMEOUT = 5000
SLOW_MO = 1000


class Test_Login_Page:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page, login_page
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=SLOW_MO)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://web.eos.bnk-il.com/auth")
        login_page = Login_page_main(page)
        yield
        context.close()
        browser.close()

    def test_wait_for_error_or_success_message(self):
        login_page.fill_email_address(USER_EMAIL)
        login_page.type_password(PASSWORD)
        login_page.submit_button()

        try:
            error_message = page.locator("text=Sign in Failed - NonJsonResponseError")
            error_message.wait_for(state="visible", timeout=TIMEOUT)

            if error_message.is_visible():
                logger.info(f"The login error message appeared as expected. user is not valid and couldn't login to"
                            f" the site!")
                assert True, f"The login error message appeared as expected. user is not valid and couldn't login to " \
                             f"the site!"

        except PlaywrightTimeoutError:
            try:
                success_message = page.locator("text=Sign in Successful")
                success_message.wait_for(state="visible", timeout=TIMEOUT)

                if success_message.is_visible():
                    logger.info("Success message appeared as expected.")
                    assert True, "Success message is visible as expected."

            except PlaywrightTimeoutError:
                logger.error("Neither error nor success message appeared within the timeout.")
                assert False, "No relevant message appeared within the timeout."
