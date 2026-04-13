"""
Тест фильтрации экскурсий по месту проведения (Москва).
"""

import time
from pages.filter_page import FilterPage

def test_filter(browser):
    filter_page = FilterPage(browser)
    filter_page.open("https://excursium.com/ekskursii-dlya-shkolnikov/list")
    time.sleep(2)

    filter_page.open_location_filter()   # открываем фильтр "Место проведения"
    filter_page.select_moscow()          # выбираем "Москва"
    time.sleep(2)

    # Проверяем, что в URL или на странице появилась Москва
    assert "moscow" in browser.current_url.lower() or "Москва" in browser.page_source

    browser.save_screenshot("screenshots/TC-06_filter_moscow.png")
