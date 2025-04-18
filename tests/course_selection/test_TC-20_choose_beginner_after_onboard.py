# -------------------------------------------------------------------------------
# --- Imports ---
# -------------------------------------------------------------------------------

import pytest
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# -------------------------------------------------------------------------------
# --- Fixture ---
# -------------------------------------------------------------------------------

from config import capabilities_options, appium_server_url  # Импортируем настройки
from locators import Languages, OnboardingPage, Course, TrainingPage, Navigation, MainPage


@pytest.fixture(scope="function")
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield android_driver
    android_driver.quit()

# -------------------------------------------------------------------------------
# --- Utils ---
# -------------------------------------------------------------------------------

def swipe_left(driver):
    size = driver.get_window_size()
    start_x = size['width'] * 0.8
    end_x = size['width'] * 0.2
    start_y = size['height'] / 2
    driver.swipe(start_x, start_y, end_x, start_y, 1000)

def wait_and_click(driver, by, value, timeout=10):
    """Ожидание элемента и клик."""
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    element.click()

def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

# -------------------------------------------------------------------------------
# --- Test ---
# -------------------------------------------------------------------------------

def test_choose_beginner_after_onboard(driver):
    sleep(7)

    # English Language
    wait_and_click(driver, *Languages.ENGLISH)

    # Выполняем свайпы
    for _ in range(3):
        swipe_left(driver)

    # Нажимаем кнопку "BEGIN TRAINING"
    wait_and_click(driver, *OnboardingPage.BTN_START)

    #Выбираем "Начальный курс"
    wait_and_click(driver, *Course.BEGINNER_COURSE)

# -------------------------------------------------------------------------------
# --- Asserts ---
# -------------------------------------------------------------------------------

    demo_balance = wait_for_element(driver, *MainPage.DEMO_BALANCE)
    assert demo_balance is not None, 'Demo balance is not found'

    change_course_btn = wait_for_element(driver, *TrainingPage.CHANGE_COURSE)
    assert change_course_btn is not None, 'Change course button is not found'

    navigation_training = wait_for_element(driver, *Navigation.TRAINING)
    assert navigation_training is not None, 'Navigation training is not found'

    navigation_trading = wait_for_element(driver, *Navigation.TRADING)
    assert navigation_trading is not None, 'Navigation trading is not found'

    navigation_broker = wait_for_element(driver, *Navigation.BROKERS)
    assert navigation_broker is not None, 'Navigation broker is not found'

    navigation_settings = wait_for_element(driver, *Navigation.SETTINGS)
    assert navigation_settings is not None, 'Navigation settings is not found'
