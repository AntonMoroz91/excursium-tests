import time
from pages.calculator_page import CalculatorPage


def test_calculator(browser):
    browser.get("https://excursium.com/ekskursii/muzey-istorii-moloka-i-glazirovannogo-syrka")
    time.sleep(3)

    calc = CalculatorPage(browser)

    try:
        old_price = calc.get_price_text()
        print(f"Цена до: {old_price}")
    except:
        print("Цена до не найдена, возможно, элемент другой")
        old_price = "0"

    calc.select_25_34()
    time.sleep(2)

    try:
        new_price = calc.get_price_text()
        print(f"Цена после: {new_price}")
    except:
        print("Цена после не найдена")
        new_price = "0"

    assert old_price != new_price, "Цена не изменилась или элемент не найден"