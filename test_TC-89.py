import pytest
import allure
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

from time import sleep, time
from appium.options.android import UiAutomator2Options

# Для автотестов использовать только телефон Motorola.
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='ZY32FX9296',  # Phone Motorola
    platformVersion='11',
    appPackage='com.tradingcourses.learnhowtoinvest',
    appActivity='com.trade.test.ui.splash.SplashActivity',
    language='en',
    locale='US'
)

capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
appium_server_url = 'http://localhost:4723'


@pytest.fixture()
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield android_driver
    if android_driver:
        android_driver.quit()


def rotate_screen(driver, orientation):
    # orientation: 'LANDSCAPE' or 'PORTRAIT'
    driver.orientation = orientation


def test_login(driver):
    sleep(7)

    # Выбираем англ язык
    english = driver.find_element(By.XPATH,
                                  '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_name" and @text="English"]')
    english.click()
    sleep(1)

    # Нажимает кнопку "Войти/Зарегистрироваться
    login = driver.find_element(By.XPATH,
                                '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_enter"]')
    login.click()
    sleep(1)

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
    signin = driver.find_element(By.XPATH,
                                 '//android.widget.Button[@resource-id="com.tradingcourses.learnhowtoinvest:id/bt_signIn"]')
    signin.click()
    sleep(3)

    # Переходим на экран треининг
    training = driver.find_element(By.XPATH,
                                   '//android.widget.FrameLayout[@content-desc="Training"]/android.widget.FrameLayout/android.widget.ImageView')
    training.click()
    sleep(1)

    # Меняем курс
    change_course = driver.find_element(By.XPATH,
                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button')
    change_course.click()
    sleep(1)

    # PRO course
    pro = driver.find_element(By.XPATH,
                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]')
    pro.click()
    sleep(1)

    # Выполняем свайп экрана вверх до указанного элемента
    while True:
        try:
            # Поиск элемента по тексту
            target_element = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Lesson 11")')
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

    # Проходим 11 урок
    lesson11 = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_title" and @text="Lesson 11"]')
    lesson11.click()
    sleep(5)

    complete_task = driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button')
    complete_task.click()
    sleep(3)

    question1 = driver.find_element(By.XPATH,'(//android.widget.ImageView[@resource-id="com.tradingcourses.learnhowtoinvest:id/iv_check"])[1]')
    question1.click()
    sleep(3)

    question2 = driver.find_element(By.XPATH,'(//android.widget.ImageView[@resource-id="com.tradingcourses.learnhowtoinvest:id/iv_check"])[1]')
    question2.click()
    sleep(3)

    question3 = driver.find_element(By.XPATH,'(//android.widget.ImageView[@resource-id="com.tradingcourses.learnhowtoinvest:id/iv_check"])[4]')
    question3.click()
    sleep(3)

    question4 = driver.find_element(By.XPATH,'(//android.widget.ImageView[@resource-id="com.tradingcourses.learnhowtoinvest:id/iv_check"])[4]')
    question4.click()
    sleep(3)

    question5 = driver.find_element(By.XPATH,'(//android.widget.ImageView[@resource-id="com.tradingcourses.learnhowtoinvest:id/iv_check"])[3]')
    question5.click()
    sleep(3)

    close_quiz = driver.find_element(By.XPATH,'//android.widget.ImageView[@resource-id="com.tradingcourses.learnhowtoinvest:id/iv_cancel"]')
    close_quiz.click()
    sleep(2)








