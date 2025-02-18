import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
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
            EC.presence_of_element_located((MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/cl_note")'))
        )
        print("Плашка найдена. Нажимаем кнопки.")
        wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_neg")')
        wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_neg")')
    except:
        print("Плашка не найдена. Продолжаем выполнение теста.")

#=============================================#

def test_login(driver):
    handle_quiz_popup(driver)
    sleep(7)

    # Выбираем англ язык
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("English")')

    # Нажимает кнопку "Войти/Зарегистрироваться
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_enter")')

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
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_signIn")')

    # Переходим на экран треининг
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/navigation_bar_item_large_label_view")')

    # Меняем курс
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_change_course")')

    # PRO course
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_course_desc2")')

    handle_quiz_popup(driver)

    # Выполняем свайп экрана вверх до указанного элемента
    while True:
        try:
            # Поиск элемента по тексту
            target_element = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("The Double Red Binary Options Trading Strategy").instance(0)')
            print("Элемент найден!")
            break  # Если элемент найден, выходим из цикла
        except:
            # Выполняем свайп вверх
            size = driver.get_window_size()
            start_x = size['width'] / 2
            start_y = size['height'] * 0.8
            end_y = size['height'] * 0.4

            driver.swipe(start_x, start_y, start_x, end_y, 800)
            print("Свайп вверх выполнен.")
            sleep(1)

    # Проходим 9 урок
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("The Double Red Binary Options Trading Strategy").instance(0)')

    # COMPLETE
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_complete")')

    # ----------------------------------------------------------------------------------------------------------
    #   ____         _            ____ ____ _____ ______ ____ ____   _  __
    #  / __ \ __ __ (_)___       / __// __// ___//_  __//  _// __ \ / |/ /
    # / /_/ // // // //_ /      _\ \ / _/ / /__   / /  _/ / / /_/ //    /
    # \___\_\\_,_//_/ /__/     /___//___/ \___/  /_/  /___/ \____//_/|_/

    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Uptrend")')
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Difference between closing and high price")')
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("PUT option")')
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Short-term price reversals")')
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Formation of two bearish candles after testing the resistance level")')
    # ----------------------------------------------------------------------------------------------------------

    # CLOSE QUIZ
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/iv_cancel")')

    handle_quiz_popup(driver)

    # Выполняем свайп экрана вверх до указанного элемента
    while True:
        try:
            # Поиск элемента по тексту
            target_element = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Select the image that contains two consecutive red candles")')
            print("Элемент найден!")
            break  # Если элемент найден, выходим из цикла
        except:
            # Выполняем свайп вверх
            size = driver.get_window_size()
            start_x = size['width'] / 2
            start_y = size['height'] * 0.8
            end_y = size['height'] * 0.4

            driver.swipe(start_x, start_y, start_x, end_y, 800)
            print("Свайп вверх выполнен.")
            sleep(1)


    # OPEN PRACTICAL
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Select the image that contains two consecutive red candles")')

    # DOWN IMAGE
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/iv_img2")')

    # CLEAR
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_ok")')

    # COMPLETE LESSON
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_start")')

    handle_quiz_popup(driver)





