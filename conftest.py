import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def browser():
    firefox_options = Options()

    # Режим инкогнито (приватный)
    firefox_options.add_argument("--private")

    # Отключаем уведомления
    firefox_options.set_preference("dom.webnotifications.enabled", False)

    # Отключаем загрузку изображений (ускоряет тесты)
    firefox_options.set_preference("permissions.default.image", 2)

    # Маскировка WebDriver (чтобы не блокировали)
    firefox_options.set_preference("dom.webdriver.enabled", False)
    firefox_options.set_preference("useAutomationExtension", False)

    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()

    yield driver
    driver.quit()