from Tests.UI.Pages.BasePage import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.drivers.chrome import ChromeDriver


class CreatedGistPage(BasePage):

    def __init__(self, driver: ChromeDriver):
        BasePage.__init__(self, driver)
        self.gist_pjax_container_id = "gist-pjax-container"
        self.gist_descr_css = "div[itemprop='about']"
        self.gist_file_name_css = "div[class='file-info']"

    def wait_for_page(self):
        (WebDriverWait(self.driver, 20)
         .until(EC.visibility_of_element_located((By.ID, self.gist_pjax_container_id))))

    def get_gist_descr(self) -> str:
        return self.get_element_by_css(self.gist_descr_css).text

    def get_gist_file_name(self) -> str:
        return self.get_element_by_css(self.gist_file_name_css).text
