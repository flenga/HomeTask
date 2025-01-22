import pytest
import logging
from playwright.sync_api import Playwright
from login_main_page import Login_page_main
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from logger import logger

logging.basicConfig(level=logging.INFO)
logger = logger()


password = '123456'
user_email = 'doron@gmail.com'
form_message = 'This is the place where I type some text in the Form!!!!'


class Test_Login_Page:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page, login_page
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://web.eos.bnk-il.com/auth")
        login_page = Login_page_main(page)
        yield

        # Teardown after tests
    def teardown_class(self):
        context.close()
        browser.close()

    # def test_wait_for_error_message(self):
    #     login_page.fill_email_address(user_email)
    #     login_page.type_password(password)
    #     login_page.login_button()
    #     try:
    #         error_message = page.locator("text=Sign in Failed - NonJsonResponseError")
    #         error_message.wait_for(timeout=5000)  # Timeout in milliseconds
    #         assert error_message.is_visible(), "Error message not visible"
    #         log_message = "Error message appeared as expected."
    #         logger.info({log_message})
    #     except PlaywrightTimeoutError:
    #         logger.info("Error message did not appear within the timeout.")
    def test_wait_for_error_or_success_message(self):
        # Fill the login form and submit
        login_page.fill_email_address(user_email)
        login_page.type_password(password)
        login_page.submit_button()

        try:
            page.wait_for_selector("text=Sign in Failed - NonJsonResponseError", timeout=5000)
            error_message = page.locator("text=Sign in Failed - NonJsonResponseError")

            if error_message.is_visible():
                logger.info("Error message appeared as expected.")
                assert True, "Error message is visible as expected."

        except PlaywrightTimeoutError:
            try:
                # Check for an alternative success message if the error does not appear
                page.wait_for_selector("text=Sign in Successful", timeout=5000)
                success_message = page.locator("text=Sign in Successful")

                if success_message.is_visible():
                    logger.info("Success message appeared as expected.")
                    assert True, "Success message is visible as expected."

            except PlaywrightTimeoutError:
                logger.error("Neither error nor success message appeared within the timeout.")
                assert False, "No relevant message appeared within the timeout."

                # Additional assertions can be added if required
            logger.info("Test case completed.")
