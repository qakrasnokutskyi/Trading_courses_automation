import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Languages, Login, TradingPage, Navigation, MainPage, TimeFrame

#=============================================#

from config import capabilities_options, appium_server_url  # Импортируем настройки

@pytest.fixture(scope="function")
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield android_driver
    if android_driver:
        android_driver.terminate_app("com.tradingcourses.learnhowtoinvest")
        android_driver.activate_app("com.tradingcourses.learnhowtoinvest")
        android_driver.quit()

def wait_and_click(driver, by, value, timeout=10):
    """Ожидание элемента и клик."""
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    element.click()


def rotate_screen(driver, orientation):
    # orientation: 'LANDSCAPE' or 'PORTRAIT'
    driver.orientation = orientation

def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

#=============================================#

def test_open_switch_timeframe(driver):
    sleep(7)

    # Выбираем англ язык
    wait_for_element(driver, *Languages.ENGLISH).click()

    # Нажимает кнопку "Войти/Зарегистрироваться
    wait_and_click(driver, *Login.BTN_REGISTRATION_LOGIN)

    # Заполняем поле email
    email = wait_for_element(driver, *Login.FIELD_EMAIL)
    email.send_keys('qakrasnokutskiy@gmail.com')

    # Заполняем поле password
    password = wait_for_element(driver, *Login.FIELD_PASSWORD)
    password.send_keys('e251dq12r')

    # Выполняем вход
    wait_and_click(driver, *Login.BTN_SIGNIN)

    # Переходим на экран c графиком
    wait_and_click(driver, *Navigation.TRADING)

    # Открываем "Таймфрейм"
    wait_and_click(driver, *TradingPage.TIMEFRAME, timeout=3)

    # Выбираем таймфрейм "S20"
    wait_and_click(driver, *TimeFrame.TIMEFRAME_S20, timeout=3)

    # Открываем "Таймфрейм"
    wait_and_click(driver, *TradingPage.TIMEFRAME, timeout=3)

    # Выбираем таймфрейм "m1"
    wait_and_click(driver, *TimeFrame.TIMEFRAME_M1, timeout=3)

    # Открываем "Таймфрейм"
    wait_and_click(driver, *TradingPage.TIMEFRAME, timeout=3)

    # Выбираем таймфрейм "m1"
    wait_and_click(driver, *TimeFrame.TIMEFRAME_M2, timeout=3)

# ==================== asserts ====================

    demo_balance = wait_for_element(driver, *MainPage.DEMO_BALANCE)
    assert demo_balance is not None, 'Demo Balance is not visible'

    currency_pairs = wait_for_element(driver, *TradingPage.CURRENCY_PAIR)
    assert currency_pairs is not None, 'CurrencyPairs is not visible'

    indicators = wait_for_element(driver, *TradingPage.INDICATORS)
    assert indicators is not None, 'Indicators is not visible'

    timeframe = wait_for_element(driver, *TradingPage.TIMEFRAME)
    assert timeframe is not None, 'Timeframe is not visible'

    btn_sell = wait_for_element(driver, *TradingPage.BUY)
    assert btn_sell is not None, 'Buy button is not visible'

    btn_buy = wait_for_element(driver, *TradingPage.SELL)
    assert btn_buy is not None, 'Sell button is not visible'