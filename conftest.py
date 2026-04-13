"""
Настройка фикстур для pytest.
Здесь создаётся и закрывается браузер перед каждым тестом.
"""

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser():
    """
    Фикстура, которая создаёт браузер перед тестом и закрывает после.
    Используется Chrome в режиме инкогнито с отключёнными уведомлениями.
    """
    chrome_options = Options()
    chrome_options.add_argument("--incognito")           # режим инкогнито
    chrome_options.add_argument("--disable-notifications")  # отключаем всплывающие уведомления

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()  # на весь экран
    yield driver              # передаём драйвер в тест
    driver.quit()             # закрываем браузер после теста
