from selenium.webdriver.common.by import By
from .base_page import BasePage

class ExcursionsListPage(BasePage):
    SHOW_MORE_BUTTON = (By.XPATH, "//button[text()='Показать больше']")
    FILTER_OPTION = (By.CSS_SELECTOR, ".filter-option")

    def click_show_more(self):
        self.click(self.SHOW_MORE_BUTTON)

    def select_filter(self, option_text):
        option = (By.XPATH, f"//span[text()='{option_text}']")
        self.click(option)