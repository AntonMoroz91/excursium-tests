import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class RegistrationPage(BasePage):
    # Локаторы
    LOGIN_ICON = (By.XPATH, "/html/body/header/nav/div/ul/li[4]/a")
    EMAIL_INPUT = (By.XPATH, "//*[@id='login-vue']/div/div[2]/div[4]/div[3]/input")
    PASSWORD_INPUT = (By.XPATH, "//*[@id='login-vue']/div/div[2]/div[4]/div[4]/div[1]/input")
    TERMS_CHECKBOX = (By.XPATH, "//*[@id='isAgreement']")
    CREATE_BUTTON = (By.XPATH, "//*[@id='registraion-btn']/span[2]")

    def open_login_icon(self):
        icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGIN_ICON)
        )
        icon.click()
        time.sleep(1)

    def open_registration_form(self):
        """Найти контейнер с кнопками и кликнуть по кнопке 'Регистрация'"""
        container = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='login-vue']/div/div[2]/div[3]/div[1]"))
        )
        buttons = container.find_elements(By.TAG_NAME, "button")
        if len(buttons) >= 2:
            buttons[1].click()  # вторая кнопка = Регистрация
        else:
            raise Exception("Кнопка 'Регистрация' не найдена")
        time.sleep(1)

    def enter_email(self, email):
        field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.EMAIL_INPUT)
        )
        field.clear()
        field.send_keys(email)

    def enter_password(self, password):
        field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.PASSWORD_INPUT)
        )
        field.clear()
        field.send_keys(password)

    def accept_terms(self):
        checkbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.TERMS_CHECKBOX)
        )
        checkbox.click()

    def click_create_account(self):
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CREATE_BUTTON)
        )
        btn.click()
        time.sleep(2)

    def is_registration_successful(self):
        return "startup" in self.driver.current_url
