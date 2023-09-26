from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.drivers.chrome import ChromeDriver

from Tests.UI.Pages.BasePage import BasePage


class NewGistPage(BasePage):
    def __init__(self, driver: ChromeDriver):
        BasePage.__init__(self, driver)
        self.page_url = "https://gist.github.com/"
        # Page elements locators
        self.gist_description_by_name = "gist[description]"
        self.gist_file_item_css = "div[class='js-gist-file']"
        self.gist_file_name_by_name = "gist[contents][][name]"
        self.gist_file_editor_css = "pre[class=' CodeMirror-line ']"
        self.add_file_button_css = "button[class='js-add-gist-file btn float-left']"
        self.gist_type_dropdown_css = "div[class='BtnGroup'] summary[aria-haspopup='menu']"
        self.gist_type_options_css = "[class='select-menu-item-heading']"
        self.gist_submit_button_css = "div[class='BtnGroup'] button[type='submit']"

    def get_description(self) -> WebElement:
        return self.get_element_by_name(self.gist_description_by_name)

    def get_file_item(self) -> WebElement:
        return self.get_element_by_css(self.gist_file_item_css)

    def get_file_name(self, file_item: WebElement) -> WebElement:
        return file_item.find_element(By.NAME,self.gist_file_name_by_name)

    def get_file_content(self, file_item) -> WebElement:
        return file_item.find_element(By.CSS_SELECTOR,self.gist_file_editor_css)

    def get_add_file_button(self) -> WebElement:
        return self.get_element_by_css(self.add_file_button_css)

    def get_type_dropdown(self) -> WebElement:
        return self.get_element_by_css(self.gist_type_dropdown_css)

    def get_type(self, text):
        types = self.driver.find_elements(By.CSS_SELECTOR, self.gist_type_options_css)
        for gist_type in types:
            print(f"type is {gist_type.text}")
            if gist_type.text == text:
                return gist_type
        return None

    def wait_for_page(self):
        (WebDriverWait(self.driver, 200)
         .until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.add_file_button_css))))





