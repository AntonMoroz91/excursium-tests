import time
import json
from pages.login_page import LoginPage

def test_login_with_registered_user(browser):
    with open("registered_user.json", "r") as f:
        user = json.load(f)

    login_page = LoginPage(browser)
    login_page.open("https://excursium.com")
    time.sleep(2)

    login_page.open_login_icon()
    time.sleep(1)

    login_page.open_login_tab()
    time.sleep(1)

    login_page.enter_email(user["email"])
    login_page.enter_password(user["password"])
    login_page.click_login_button()

    assert login_page.is_login_successful(), "Не удалось войти"

    browser.save_screenshot("screenshots/TC-04_login_success.png")
