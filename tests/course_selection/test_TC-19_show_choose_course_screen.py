# -------------------------------------------------------------------------------
# --- Imports ---
# -------------------------------------------------------------------------------

import pytest
from locators import Languages, OnboardingPage, Course
from appium import webdriver
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

def test_show_choose_course_screen(driver):
    sleep(7)

    # English Language
    wait_and_click(driver, *Languages.ENGLISH)

    # Выполняем свайпы
    for _ in range(3):
        swipe_left(driver)

    #Нажимаем кнопку "BEGIN TRAINING"
    wait_and_click(driver, *OnboardingPage.BTN_START)

# -------------------------------------------------------------------------------
# --- Asserts ---
# -------------------------------------------------------------------------------

    begin_course = wait_for_element(driver, *Course.BEGINNER_COURSE)
    assert begin_course is not None, 'Course "Beginner" is not found'

    middle_course = wait_for_element(driver, *Course.MIDDLE_COURSE)
    assert middle_course is not None, 'Course "Middle" is not found'

    advanced_course = wait_for_element(driver, *Course.ADVANCED_COURSE)
    assert advanced_course is not None, 'Course "Advanced" is not found'

    pro_course = wait_for_element(driver, *Course.PRO_COURSE)
    assert pro_course is not None, 'Course "Pro" is not found'

    choose_course_title = wait_for_element(driver, *Course.CHOOSE_COURSE_TITLE)
    assert choose_course_title is not None, 'Choose course title is not found'