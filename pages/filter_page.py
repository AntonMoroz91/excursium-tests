from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class FilterPage(BasePage):
    # Локаторы
    LOCATION_FILTER = (By.XPATH, "/html/body/main/div/section[2]/div/div/aside/div/div[2]/form/div[5]/p/button")
    OPTION_MOSCOW = (By.XPATH, "//label[contains(text(), 'Москва')]")

    def open_location_filter(self):
        loc = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOCATION_FILTER)
        )
        loc.click()

    def select_moscow(self):
        moscow = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.OPTION_MOSCOW)
        )
        moscow.click()