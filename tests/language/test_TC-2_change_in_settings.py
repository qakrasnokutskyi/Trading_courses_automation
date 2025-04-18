# -------------------------------------------------------------------------------
# --- Imports ---
# -------------------------------------------------------------------------------

import pytest
from appium import webdriver
from time import sleep
from locators import Languages, OnboardingPage, Course, Navigation, SettingsPage, MainPage
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

def rotate_screen(driver, orientation):
    # orientation: 'LANDSCAPE' or 'PORTRAIT'
    driver.orientation = orientation

def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

# -------------------------------------------------------------------------------
# --- Test ---
# -------------------------------------------------------------------------------

def test_change_in_settings(driver):
    sleep(7)

    # English Language
    wait_and_click(driver, *Languages.ENGLISH)

    # Skip onboard - display
    wait_and_click(driver, *OnboardingPage.BTN_START)

    # Choose 'BEGINNER' course
    wait_and_click(driver, *Course.BEGINNER_COURSE)

    # Переходим в настройки
    wait_and_click(driver, *Navigation.SETTINGS)

    # Выбираем смену языка
    wait_and_click(driver, *SettingsPage.CHANGE_LANGUAGE)

    # Выбираем Русский язык
    wait_and_click(driver, *Languages.RUSSIAN)

    # Переходим в настройки
    wait_and_click(driver, *Navigation.SETTINGS_RU)

    # Выбираем смену языка
    wait_and_click(driver, *SettingsPage.CHANGE_LANGUAGE)

    # Выбираем Украинский язык
    wait_and_click(driver, *Languages.UKRAINE)

    # Переходим в настройки
    wait_and_click(driver, *Navigation.SETTINGS_UA)

    # Выбираем смену языка
    wait_and_click(driver, *SettingsPage.CHANGE_LANGUAGE)

    # Выбираем Немецкий язык
    wait_and_click(driver, *Languages.DEUTSCH)

    # Переходим в настройки
    wait_and_click(driver, *Navigation.SETTINGS_DE)

    # Выбираем смену языка
    wait_and_click(driver, *SettingsPage.CHANGE_LANGUAGE)

    # Выбираем Индонезийский язык
    wait_and_click(driver, *Languages.INDONESIA)

    # Переходим в настройки
    wait_and_click(driver, *Navigation.SETTINGS_ID)

    # Выбираем смену языка
    wait_and_click(driver, *SettingsPage.CHANGE_LANGUAGE)

    # Выбираем Урду язык
    wait_and_click(driver, *Languages.URDU)

    # Переходим в настройки
    wait_and_click(driver, *Navigation.SETTINGS_UR)

    # Выбираем смену языка
    wait_and_click(driver, *SettingsPage.CHANGE_LANGUAGE)

    # Выбираем Хинди язык
    wait_and_click(driver, *Languages.HINDI)

# -------------------------------------------------------------------------------
# --- Asserts ---
# -------------------------------------------------------------------------------

    demo_balance_hindi = wait_for_element(driver, *MainPage.DEMO_BALANCE)
    assert demo_balance_hindi is not None, 'Demo_Balance_Hindi is not found'

    training_hindi_language = wait_for_element(driver, *Navigation.TRAINING_HI)
    assert training_hindi_language is not None, 'Trainiing_Hindi is not found'

    trading_hindi_language = wait_for_element(driver, *Navigation.TRADING_HI)
    assert trading_hindi_language is not None, 'Trading_Hindi is not found'

    brokers_hindi_language = wait_for_element(driver, *Navigation.BROKERS_HI)
    assert brokers_hindi_language is not None, 'Brokers_Hindi is not found'

    settings_hindi_language = wait_for_element(driver, *Navigation.SETTINGS_HI)
    assert settings_hindi_language is not None, 'Settings_Hindi is not found'