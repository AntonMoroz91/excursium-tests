"""
Базовый класс для всех страниц (Page Object Model).
Содержит общие методы для работы с элементами.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # ожидание до 10 секунд

    def open(self, url):
        """Открыть указанный URL в браузере"""
        self.driver.get(url)

    def find_element(self, locator):
        """Найти один элемент с ожиданием его появления"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """Кликнуть по элементу"""
        self.find_element(locator).click()

    def input_text(self, locator, text):
        """Очистить поле и ввести текст"""
        el = self.find_element(locator)
        el.clear()
        el.send_keys(text)

    def get_text(self, locator):
        """Получить текст элемента"""
        return self.find_element(locator).text

    def save_screenshot(self, filename):
        """Сохранить скриншот в папку screenshots/"""
        self.driver.save_screenshot(f"screenshots/{filename}")
