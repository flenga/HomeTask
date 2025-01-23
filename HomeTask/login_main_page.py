from logger import logger


class Login_page_main:
    EMAIL_INPUT = "input[id=':r1:']"
    EMAIL_ERROR_MESSAGE = "//p[@id=':r1:-helper-text']"
    PASSWORD_INPUT = "input[placeholder='Password']"
    PASSWORD_ERROR_MESSAGE = "//p[@id=':r2:-helper-text']"
    LOGIN_BUTTON = "//span[normalize-space()='Login']"
    ERROR_DIALOG = "Sign in Failed -"

    def __init__(self, page):
        self.page = page
        self.email_address = self.page.locator(self.EMAIL_INPUT)
        self.email_address_error_message = self.page.locator(self.EMAIL_ERROR_MESSAGE)
        self.password = self.page.locator(self.PASSWORD_INPUT)
        self.password_error_message = self.page.locator(self.PASSWORD_ERROR_MESSAGE)
        self.login_button = self.page.locator(self.LOGIN_BUTTON)

    def fill_email_address(self, email):
        logger.info(f"Filling email address: {email}")
        self.email_address.fill(email)

    def type_password(self, textarea):
        logger.info("Typing password.")
        self.password.fill(textarea)

    def submit_button(self):
        logger.info("Submitting login button.")
        self.login_button.click()
