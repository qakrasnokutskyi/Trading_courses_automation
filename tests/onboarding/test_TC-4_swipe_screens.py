# -------------------------------------------------------------------------------
# --- Imports ---
# -------------------------------------------------------------------------------

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# -------------------------------------------------------------------------------
# --- Fixture ---
# -------------------------------------------------------------------------------

from config import capabilities_options, appium_server_url  # Импортируем настройки

@pytest.fixture(scope="function")
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield android_driver
    android_driver.quit()

# -------------------------------------------------------------------------------
# --- Utils ---
# -------------------------------------------------------------------------------

def wait_and_click(driver, by, value, timeout=10):
    """Ожидание элемента и клик."""
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    element.click()

def swipe_left(driver):
    size = driver.get_window_size()
    start_x = size['width'] * 0.8
    end_x = size['width'] * 0.2
    start_y = size['height'] / 2
    driver.swipe(start_x, start_y, end_x, start_y, 1000)

def rotate_screen(driver, orientation):
    # orientation: 'LANDSCAPE' or 'PORTRAIT'
    driver.orientation = orientation

# -------------------------------------------------------------------------------
# --- Test ---
# -------------------------------------------------------------------------------

def test_swipe_screens(driver):
    sleep(7)

    # English Language
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("English")')

    # Выполняем свайпы
    for _ in range(3):
        swipe_left(driver)

# -------------------------------------------------------------------------------
# --- Asserts ---
# -------------------------------------------------------------------------------