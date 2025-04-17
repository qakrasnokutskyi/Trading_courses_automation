import pytest
from appium import webdriver
from time import sleep, time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Languages, Login, Navigation, BrokerPage

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

def test_open_brokers_screen(driver):
    sleep(7)

    # Выбираем англ язык
    wait_and_click(driver, *Languages.ENGLISH)

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

    # Переходим в раздел Брокеры
    wait_and_click(driver, *Navigation.BROKERS)

# ==================== asserts ====================

    title_brokers_page = wait_for_element(driver, *BrokerPage.TITLE_BROKERS)
    assert title_brokers_page is not None,'Title is not visible'

    min_deposit_page = wait_for_element(driver, *BrokerPage.MIN_DEPOSIT)
    assert min_deposit_page is not None,'Min Deposit is not visible'

    rating_page = wait_for_element(driver, *BrokerPage.RATING)
    assert rating_page is not None,'Rating is not visible'

    btn_next_broker = wait_for_element(driver, *BrokerPage.BTN_NEXT_BROKER)
    assert btn_next_broker is not None,'Next Broker is not visible'

    date_brokers_page = wait_for_element(driver, *BrokerPage.DATE_BROKERS)
    assert date_brokers_page is not None,'Date Brokers is not visible'
