from selenium.webdriver.common.by import By
from .base_page import BasePage

class CalculatorPage(BasePage):
    # Локаторы
    BUTTON_25_34 = (By.XPATH, "//*[@id='detail-vue']/section[3]/div/div/div[2]/div/div[1]/div/div[3]/div/label[2]")
    PRICE = (By.XPATH, "//*[@id='container-price']")

    def select_25_34(self):
        """Выбор группы 25-34 года"""
        btn = self.find_element(self.BUTTON_25_34)
        self.driver.execute_script("arguments[0].click();", btn)

    def get_price_text(self):
        """Получить текст с ценой"""
        return self.get_text(self.PRICE)
