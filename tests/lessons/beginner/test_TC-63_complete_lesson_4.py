# -------------------------------------------------------------------------------
# --- Imports ---
# -------------------------------------------------------------------------------

import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
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
    if android_driver:
        android_driver.terminate_app("com.tradingcourses.learnhowtoinvest")
        android_driver.activate_app("com.tradingcourses.learnhowtoinvest")
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

# -------------------------------------------------------------------------------
# --- Test ---
# -------------------------------------------------------------------------------

def test_complete_lesson_4(driver):
    sleep(7)

    # Выбираем англ язык
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("English")')

    # Нажимает кнопку "Войти/Зарегистрироваться
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_enter")')

    # Заполняем поле email
    email = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Your email"]')
    email.send_keys('qakrasnokutskiy@gmail.com')
    sleep(1)
    print('Поле успешно заполнено')

    # Заполняем поле password
    password = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Your password"]')
    password.send_keys('e251dq12r')
    sleep(1)
    print('Поле успешно заполнено')

    # Выполняем вход
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_signIn")')

    # Переходим на экран треининг
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/navigation_bar_item_large_label_view")')

    # Меняем курс
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_change_course")')

    # begginer course
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_course_old_price")')

    # Выполняем свайп экрана вверх до указанного элемента
    while True:
        try:
            # Проверяем наличие элемента
            target_element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Trend Lines for Binary Options")')
            print("Элемент найден!")
            break  # Если элемент найден, выходим из цикла
        except:
            # Если элемент не найден, выполняем свайп вверх
            size = driver.get_window_size()
            start_x = size['width'] / 2
            start_y = size['height'] * 0.7  # Начальная точка свайпа (80% от высоты экрана)
            end_y = size['height'] * 0.5  # Конечная точка свайпа (20% от высоты экрана)

            driver.swipe(start_x, start_y, start_x, end_y, 800)
            print("Свайп вверх выполнен.")
            sleep(1)  # Небольшая задержка перед следующим свайпом


    # Проходим урок 4
    wait_and_click(driver,AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Trend Lines for Binary Options")')

    # button 'complete'
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_complete")')

    # trend predictor - buttin "CALL"
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_call")')

    # button 'CLEAR'
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_ok")')

    # bytton 'continue'
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_start")')

# -------------------------------------------------------------------------------
# --- Asserts ---
# -------------------------------------------------------------------------------