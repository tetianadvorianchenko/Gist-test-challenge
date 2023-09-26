from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    page_url =""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.implicit_wait = 25

    def get_element_by_name(self, locator) -> WebElement:
        return self.driver.find_element(By.NAME, locator)
    def get_element_by_css(self, locator) -> WebElement:
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def get_element_by_xpath(self, locator) -> WebElement:
        return self.driver.find_element(By.XPATH, locator)

    def get_element_by_id(self, locator) -> WebElement:
        return self.driver.find_element(By.ID, locator)

    def open_page(self):
        self.driver.get(self.page_url)


