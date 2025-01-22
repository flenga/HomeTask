import allure


class Main_login_page:
    def __init__(self, page):
        self.page = page
        self.first_section_in_page_buttons = self.page.locator('div.et_pb_button_module_wrapper a')
        self.facebook_links = self.page.locator("a[title*='Follow on Facebook']")
        self.get_attribute_fro_element = self.page
        self.form_third_section = self.page.locator("#et_pb_contact_form_0 > div.et_pb_contact > form")
        self.first_name = self.page.locator("input[id='et_pb_contact_name_0']")
        self.email_address = self.page.locator("input[id='et_pb_contact_email_0']")
        self.free_text_textarea = self.page.locator("textarea[id='et_pb_contact_message_0']")
        self.question_section = self.form_third_section.locator('[class ="clearfix"]').inner_text()
        self.sum_input_field = self.form_third_section.locator('input[class="input et_pb_contact_captcha"]')
        self.success_message = '//*[@id="et_pb_contact_form_0"]/div'
        # self.close_dialog_button = self.page.locator("#div.formkit-slide-in")
        self.submit_button = self.form_third_section.locator('button[type="submit"]')

    def wait_for_element_visible(self, selector: str):
        self.page.wait_for_selector(selector, state='visible')

    def count_elements_of_selector(self) -> int:
        return self.first_section_in_page_buttons.count()

    @allure.step('get all Facebook links in page')
    def get_all_facebook_links(self) -> str:
        return self.facebook_links

    @allure.step("Fill first name in field - first name")
    def fill_first_name(self, first_name):
        self.first_name.fill(first_name)

    @allure.step("Fill email in email field")
    def fill_email_address(self, email):
        self.email_address.fill(email)

    @allure.step("Fill message in textarea field")
    def fill_textarea(self, textarea):
        self.free_text_textarea.fill(textarea)

    @allure.step("Fill the captcha")
    def fill_form_captcha(self):
        expression = eval(self.question_section.replace('=', ''))
        self.sum_input_field.fill(str(expression))

    @allure.step("Submit form button")
    def submit_form(self):
        self.submit_button.click()

    @allure.step("Check that the success message appear in place")
    def check_success_message_after_submit_form(self):
        return self.page.wait_for_select