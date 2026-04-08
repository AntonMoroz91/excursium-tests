from selenium.webdriver.common.by import By
from .base_page import BasePage

class ExcursionDetailPage(BasePage):
    PERSON_COUNT = (By.ID, "person_count")
    TOTAL_PRICE = (By.CSS_SELECTOR, ".total-price")
    ERROR_MSG = (By.CSS_SELECTOR, ".error")

    def set_person_count(self, count):
        self.input_text(self.PERSON_COUNT, str(count))

    def get_total_price(self):
        return self.get_text(self.TOTAL_PRICE)

    def get_error(self):
        return self.get_text(self.ERROR_MSG)