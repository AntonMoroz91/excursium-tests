from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class RegistrationPage(BasePage):
    EMAIL = (By.XPATH, "//*[@id='login-vue']/div/div[2]/div[4]/div[3]/input")
    PASSWORD = (By.XPATH, "//*[@id='login-vue']/div/div[2]/div[4]/div[4]/div[1]/input")
    CHECKBOX = (By.XPATH, "//*[@id='isAgreement']")
    REGISTER_BUTTON = (By.XPATH, "//*[@id='login-vue']/div/div[2]/div[4]/div[1]/button[2]")

    def register(self, email, password):
        # Поле Email
        email_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.EMAIL)
        )
        email_field.clear()
        email_field.send_keys(email)

        # Поле Пароль
        pass_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PASSWORD)
        )
        pass_field.clear()
        pass_field.send_keys(password)

        # Чекбокс (клик через JavaScript)
        checkbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.CHECKBOX)
        )
        self.driver.execute_script("arguments[0].click();", checkbox)

        # Кнопка регистрации (клик через JavaScript)
        reg_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.REGISTER_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", reg_button)