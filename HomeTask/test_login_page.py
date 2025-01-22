
from time import sleep
import pytest
import allure
from playwright.sync_api import Playwright, ElementHandle
#from task_2_graphhopper_api.test_get_route import logger
from HomeTask.Login_page import Main_login_page

# Variables to use during test
#  1
number_of_buttons_in_section = 12
# test 2
expected_facebook_url_to_compare = "https://www.facebook.com/Ultimateqa1/"
# test 3
form_first_name = 'doron'
form_email = 'doron@gmail.com'
form_message = 'This is the place where I type some text in the Form!!!!'
expected_success_message = 'Thanks for contacting us'


class Test_ultimateqa_page:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, playwright: Playwright):
        global browser, context, page, ultimateqa_page
        browser = playwright.chromium.launch(headless=False, channel="chrome", slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        # page.set_default_timeout(6000)
        page.goto("https://web.eos.bnk-il.com/auth.")
        ultimateqa_page = Main_login_page(page)

    def teardown_class(self):
        context.close()
        browser.close()

    @allure.title("test count the buttons in the first section")
    @allure.description("This test count all buttons in the first section ")
    def test_count_buttons_in_element(self):
        try:
            actual_buttons_in_section = ultimateqa_page.count_elements_of_selector()
            print(f'There are {str(actual_buttons_in_section)} buttons in this section')
            assert actual_buttons_in_section == number_of_buttons_in_section
            log_message = f'assert for {number_of_buttons_in_section} Pass'
            logger.info(f'the element : {actual_buttons_in_section} is equal to what we expected')
            allure.attach(log_message, name='number of buttons in section- PASS',
                          attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            logger.error({pytest.fail("Test failed, see details", str(e))})
            allure.attach(pytest.fail(f'Test failed, see details", str(e)'),
                          name=f'success message after form being sent- FAILED',
                          attachment_type=allure.attachment_type.TEXT)

    @allure.title("social media section - verify all facebook links")
    @allure.description("This test verify all Facebook button has the correct link: "
                        "`https://www.facebook.com/Ultimateqa1/`")
    def test_verify_all_facebook_links(self):
        try:
            links = ultimateqa_page.get_all_facebook_links()
            for i in range(links.count()):
                assert links.nth(i).get_attribute('href') == expected_facebook_url_to_compare
                log_message = f'assert for {expected_facebook_url_to_compare} Pass'
                logger.info({log_message})
                allure.attach(log_message, name='success message Facebook links- PASS',
                              attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            logger.error({pytest.fail("Test failed, see details", str(e))})
            allure.attach(pytest.fail("Test failed, see details", str(e)), name='success message after form being '
                          'sent- FAILED', attachment_type=allure.attachment_type.TEXT)

    @allure.title("Test submit form in the ` Section of Random Stuff` section ")
    @allure.description("This test check the ability to submit a form by fill all relevant fields including fields: "
                        "name, email, a free input text , type of captcha and submit button and finally verifying the "
                        "success submit by asserting the success message.")
    def test_fill_a_random_form_and_verify_message(self):
        try:
            ultimateqa_page.fill_first_name(form_first_name)
            ultimateqa_page.fill_email_address(form_email)
            ultimateqa_page.fill_textarea(form_message)
            ultimateqa_page.fill_form_captcha()
            ultimateqa_page.submit_form()
            # sleep(2)
            success_message = ultimateqa_page.check_success_message_after_submit_form()
            assert success_message == expected_success_message
            log_message = f'assert for {success_message}'
            logger.info({log_message})
            allure.attach(log_message, name='success message after form being sent- PASS',
                          attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            logger.error(f'Test failed, see details', str(e))
            allure.attach(pytest.fail(f'Test failed, see details', str(e)),
                          name='success message after form being sent- FAILED',
                          attachment_type=allure.attachment_type.TEXT)