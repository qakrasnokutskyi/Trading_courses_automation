import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep, time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

def handle_quiz_popup(driver):
    """Обработка плашки после прохождения квиза."""
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/cl_note")'))
        )
        print("Плашка найдена. Нажимаем кнопки.")
        wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_neg")')
        wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_neg")')
    except:
        print("Плашка не найдена. Продолжаем выполнение теста.")

#=============================================#

def test_login(driver):
    sleep(7)

    # Выбираем англ язык
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("English")')

    # Нажимает кнопку "Войти/Зарегистрироваться
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_enter")')

    # Заполняем поле email
    email = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Your email"]')
    email.send_keys('qakrasnokutskiy@gmail.com')
    sleep(1)


    # Заполняем поле password
    password = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Your password"]')
    password.send_keys('e251dq12r')
    sleep(1)


    # Выполняем вход
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_signIn")')

    # Переходим на экран треининг
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/navigation_bar_item_large_label_view")')

    # Меняем курс
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_change_course")')

    # middle course
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_course_desc4")')

    # Проходим 1 урок
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("How the size of your deposit affects your success in trading").instance(0)')

    # close display
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/iv_cancel")')

    # open quiz
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("How the size of your deposit affects your success in trading").instance(1)')

    # ----------------------------------------------------------------------------------------------------------
    #   ____         _            ____ ____ _____ ______ ____ ____   _  __
    #  / __ \ __ __ (_)___       / __// __// ___//_  __//  _// __ \ / |/ /
    # / /_/ // // // //_ /      _\ \ / _/ / /__   / /  _/ / / /_/ //    /
    # \___\_\\_,_//_/ /__/     /___//___/ \___/  /_/  /___/ \____//_/|_/

    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("60%")')
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("1-2%")')
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("the convenient deposit amount required for trading")')
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("20-30%")')
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("no, it is very risky")')

    # ----------------------------------------------------------------------------------------------------------

    # complete lesson
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_start")')