"""
Страница со списком экскурсий и фильтрацией.
Содержит методы для работы с фильтром "Место проведения".
"""

import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

class FilterPage(BasePage):
    # Локаторы
    LOCATION_FILTER = (By.XPATH, "//button[contains(text(), 'Место проведения')]")
    MOSCOW_CHECKBOX = (By.XPATH, "//label[contains(text(), 'Москва')]")
    SHOW_MORE_BUTTON = (By.XPATH, "//button[contains(text(), 'Показать больше')]")

    def open_location_filter(self):
        """Открыть фильтр 'Место проведения' (клик через JS, чтобы избежать перекрытия)"""
        loc = self.find_element(self.LOCATION_FILTER)
        self.driver.execute_script("arguments[0].click();", loc)
        time.sleep(1)

    def select_moscow(self):
        """Выбрать 'Москва' в фильтре (клик через JS)"""
        moscow = self.find_element(self.MOSCOW_CHECKBOX)
        self.driver.execute_script("arguments[0].click();", moscow)
        time.sleep(1)

    def click_show_more(self):
        """Нажать кнопку 'Показать больше' для раскрытия всех опций"""
        more = self.find_element(self.SHOW_MORE_BUTTON)
        more.click()
        time.sleep(1)
