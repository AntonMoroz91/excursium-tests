"""
Страница авторизации (входа в личный кабинет).
Содержит методы для открытия формы входа, ввода данных и проверки успеха.
"""

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class LoginPage(BasePage):
    # Локаторы
    LOGIN_ICON = (By.XPATH, "/html/body/header/nav/div/ul/li[4]/a")
    EMAIL_INPUT = (By.XPATH, "//*[@id='login-vue']/div/div[2]/div[3]/div[3]/input")
    PASSWORD_INPUT = (By.XPATH, "//*[@id='login-vue']/div/div[2]/div[3]/div[4]/div/input")
    LOGIN_TAB_BUTTON = (By.XPATH, "//*[@id='login-vue']/div/div[2]/div[3]/div[1]/button[1]")
    SUBMIT_BUTTON = (By.XPATH, "//*[@id='login-btn']/span[2]")

    def open_login_icon(self):
        """Нажать на иконку пользователя (открывает форму логина/регистрации)"""
        icon = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LOGIN_ICON))
        icon.click()
        time.sleep(1)

    def open_login_tab(self):
        """Переключиться на вкладку 'Вход' (по умолчанию может быть 'Регистрация')"""
        btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LOGIN_TAB_BUTTON))
        btn.click()
        time.sleep(1)

    def enter_email(self, email):
        """Ввести email в поле формы входа"""
        field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.EMAIL_INPUT))
        field.click()
        field.clear()
        field.send_keys(email)

    def enter_password(self, password):
        """Ввести пароль в поле формы входа"""
        field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        field.click()
        field.clear()
        field.send_keys(password)

    def click_login_button(self):
        """Нажать кнопку 'Войти' (клик через JS для надёжности)"""
        btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SUBMIT_BUTTON))
        self.driver.execute_script("arguments[0].click();", btn)
        time.sleep(2)

    def is_login_successful(self):
        """Проверка успешного входа: в URL не должно быть 'login' или 'login-vue'"""
        current_url = self.driver.current_url
        return "login" not in current_url and "login-vue" not in current_url
