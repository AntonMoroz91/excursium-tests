import pytest
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def browser():
    firefox_options = Options()

    # Только самое важное
    firefox_options.add_argument("--private")
    firefox_options.set_preference("dom.webnotifications.enabled", False)
    firefox_options.set_preference("dom.webdriver.enabled", False)
    firefox_options.set_preference("useAutomationExtension", False)
    firefox_options.set_preference("general.useragent.override",
                                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0")

    driver = webdriver.Firefox(options=firefox_options)
    driver.maximize_window()

    yield driver

    time.sleep(3)
    driver.quit()
