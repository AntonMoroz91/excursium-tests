import time
from pages.main_page import MainPage
from pages.login_page import LoginPage
from test_data import TEST_EMAIL, TEST_PASSWORD

def test_login(browser):
    main_page = MainPage(browser)
    main_page.open("https://excursium.com")
    main_page.click(main_page.USER_ICON)
    time.sleep(2)
    login_page = LoginPage(browser)
    login_page.login(TEST_EMAIL, TEST_PASSWORD)
    time.sleep(2)  # подождать после клика
    assert "excursium" in browser.current_url