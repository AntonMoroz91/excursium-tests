import time
from pages.filter_page import FilterPage

def test_filter(browser):
    filter_page = FilterPage(browser)
    filter_page.open("https://excursium.com/ekskursii-dlya-shkolnikov/list")
    time.sleep(2)

    filter_page.open_location_filter()
    filter_page.select_moscow()
    time.sleep(2)

    assert "moscow" in browser.current_url.lower() or "Москва" in browser.page_source

    browser.save_screenshot("screenshots/TC-06_filter_moscow.png")
