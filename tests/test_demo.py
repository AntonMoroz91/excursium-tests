from pages.main_page import MainPage

def test_open_main_page(browser):
    page = MainPage(browser)
    page.open("https://excursium.com")
    assert "excursium" in browser.current_url