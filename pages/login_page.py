from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    # Локаторы
    EMAIL_INPUT = (By.XPATH, "//*[@id='login-vue']/div/div[2]/div[3]/div[3]/input")
    PASSWORD_INPUT = (By.XPATH, "//*[@id='login-vue']/div/div[2]/div[3]/div[4]/div/input")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='login-btn']")

    def login(self, email, password):
        self.input_text(self.EMAIL_INPUT, email)
        self.input_text(self.PASSWORD_INPUT, password)
        # Клик через JavaScript (обходит перекрытие)
        button = self.find_element(self.LOGIN_BUTTON)
        self.driver.execute_script("arguments[0].click();", button)