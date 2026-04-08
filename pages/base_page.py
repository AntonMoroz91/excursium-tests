from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.find_element(locator).click()

    def input_text(self, locator, text):
        el = self.find_element(locator)
        el.clear()
        el.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def save_screenshot(self, filename):
        self.driver.save_screenshot(f"screenshots/{filename}")