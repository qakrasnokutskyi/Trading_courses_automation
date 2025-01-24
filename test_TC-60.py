import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep, time

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
    """Ожидание видимости элемента и выполнение клика."""
    element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    element.click()


def rotate_screen(driver, orientation):
    # orientation: 'LANDSCAPE' or 'PORTRAIT'
    driver.orientation = orientation

#=============================================#

def test_login(driver):
    sleep(7)

    # Выбираем англ язык
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("English")')

    # Нажимает кнопку "Войти/Зарегистрироваться
    login = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_enter"]')
    login.click()
    sleep(1)

    # Заполняем поле email
    email = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Your email"]')
    email.send_keys('qakrasnokutskiy@gmail.com')
    sleep(1)


    # Заполняем поле password
    password = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Your password"]')
    password.send_keys('e251dq12r')
    sleep(1)


    # Выполняем вход
    signin = driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.tradingcourses.learnhowtoinvest:id/bt_signIn"]')
    signin.click()
    sleep(3)

   # Переходим на экран треининг
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/navigation_bar_item_large_label_view")')

    # Меняем курс
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_change_course")')

    # begginer course
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_course_old_price")')

    # Проходим 1 урок
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("What are Binary Options?").instance(0)')

    # Закрываем урок (ждем, пока кнопка станет видимой и кликабельной)
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/iv_cancel")')

    #open quiz
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("What are Binary Options?").instance(1)')

    # ----------------------------------------------------------------------------------------------------------
    #   ____         _            ____ ____ _____ ______ ____ ____   _  __
    #  / __ \ __ __ (_)___       / __// __// ___//_  __//  _// __ \ / |/ /
    # / /_/ // // // //_ /      _\ \ / _/ / /__   / /  _/ / / /_/ //    /
    # \___\_\\_,_//_/ /__/     /___//___/ \___/  /_/  /___/ \____//_/|_/

    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("A deal that is based on the movement of assets or currencies")')
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("A person who operates on a financial or stock market")')
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("A company that provides access to the exchange market and trading tools for traders")')

    # ----------------------------------------------------------------------------------------------------------

    # complete lesson
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_start")')