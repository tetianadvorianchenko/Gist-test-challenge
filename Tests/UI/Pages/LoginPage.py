from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.drivers.chrome import ChromeDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Tests.UI.Pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver: ChromeDriver):
        BasePage.__init__(self, driver)
        self.page_url = "https://github.com/login"
        # Page elements locators
        self.login_field_id = "login_field"
        self.password_field_id = "password"
        self.submit_button_by_name = "commit"

    def fill_login_field(self, value):
        self.get_element_by_id(self.login_field_id).send_keys(value)

    def fill_password_field(self, value):
        self.get_element_by_id(self.password_field_id).send_keys(value)

    def user_login(self, login, password):
        self.fill_login_field(login)
        self.fill_password_field(password)
        self.get_element_by_name(self.submit_button_by_name).click()

    def wait_for_page(self):
        (WebDriverWait(self.driver, 20)
         .until(EC.visibility_of_element_located((By.ID, self.login_field_id))))


