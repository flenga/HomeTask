# import allure


class Login_page_main:
    def __init__(self, page):
        self.page = page
        self.email_address = self.page.locator("input[id=':r1:']")
        self.email_address_error_message = self.page.locator("//p[@id=':r1:-helper-text']")
        self.password = self.page.locator("input[placeholder='Password']")
        self.password_error_message = self.page.locator("/p[@id=':r2:-helper-text']")
        self.login_button = self.page.locator("//span[normalize-space()='Login']")
        # self.log_in_error_dialog = self.page.loctor("Sign in Failed -")

    def fill_email_address(self, email):
        self.email_address.fill(email)

    def type_password(self, textarea):
        self.password.fill(textarea)

    def submit_button(self):
        self.login_button.click()