from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class CalculatorPage(BasePage):
    BUTTON_25_34 = (By.XPATH, "//*[@id='detail-vue']/section[3]/div/div/div[2]/div/div[1]/div/div[3]/div/label[2]")
    PRICE = (By.XPATH, "//*[@id='container-price']")

    def select_25_34(self):
        # Пробуем клик через JavaScript, если обычный клик не работает
        btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.BUTTON_25_34)
        )
        self.driver.execute_script("arguments[0].click();", btn)

    def get_price_text(self):
        price = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PRICE)
        )
        return price.text