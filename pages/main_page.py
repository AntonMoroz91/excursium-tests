from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage):
    # Локаторы
    SEARCH_FIELD = (By.CSS_SELECTOR, "input[placeholder*='Поиск']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    USER_ICON = (By.XPATH, "/html/body/header/nav/div/ul/li[4]")

    def search(self, text=""):
        self.input_text(self.SEARCH_FIELD, text)
        self.click(self.SEARCH_BUTTON)