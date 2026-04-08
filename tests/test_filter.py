import time
from pages.filter_page import FilterPage

def test_filter(browser):
    filter_page = FilterPage(browser)
    filter_page.open("https://excursium.com/ekskursii-dlya-shkolnikov/list")
    time.sleep(2)

    filter_page.open_location_filter()
    time.sleep(1)

    filter_page.select_moscow()
    time.sleep(2)

    assert "ekskursii-dlya-shkolnikov/list" in browser.current_url