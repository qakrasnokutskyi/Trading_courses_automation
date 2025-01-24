import pytest
import random
import string
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from faker import Faker
from time import sleep, time

#=============================================#

# Создаем экземпляр Faker для генерации данных
fake = Faker()

def generate_random_password(length=10):
    # Генерация случайного пароля с латинскими буквами и цифрами
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

#=============================================#

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

#=============================================#

def test_login(driver):
    sleep(7)

    # Выбираем англ язык
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("English")')

    # Выполнение свайпа влево между разделами онбоард страницы
    # Получаем координаты элементов для свайпа
    element = driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout')
    size = driver.get_window_size()

    # Начальные и конечные координаты для свайпа влево
    start_x = size['width'] * 0.8  # Начальная точка (80% от ширины экрана)
    end_x = size['width'] * 0.2  # Конечная точка (20% от ширины экрана)
    start_y = size['height'] / 2  # Центр экрана по высоте

    # Свайп с использованием метода swipe() (если используется более старая версия Appium)
    driver.swipe(start_x, start_y, end_x, start_y, 1000)  # Время свайпа - 1000 миллисекунд
    sleep(1)

    # Получаем координаты элементов для свайпа
    element = driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout')
    size = driver.get_window_size()

    # Начальные и конечные координаты для свайпа влево
    start_x = size['width'] * 0.8  # Начальная точка (80% от ширины экрана)
    end_x = size['width'] * 0.2  # Конечная точка (20% от ширины экрана)
    start_y = size['height'] / 2  # Центр экрана по высоте

    # Свайп с использованием метода swipe() (если используется более старая версия Appium)
    driver.swipe(start_x, start_y, end_x, start_y, 1000)  # Время свайпа - 1000 миллисекунд
    sleep(1)

    # Получаем координаты элементов для свайпа
    element = driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout')
    size = driver.get_window_size()

    # Начальные и конечные координаты для свайпа влево
    start_x = size['width'] * 0.8  # Начальная точка (80% от ширины экрана)
    end_x = size['width'] * 0.2  # Конечная точка (20% от ширины экрана)
    start_y = size['height'] / 2  # Центр экрана по высоте

    # Свайп с использованием метода swipe() (если используется более старая версия Appium)
    driver.swipe(start_x, start_y, end_x, start_y, 1000)  # Время свайпа - 1000 миллисекунд
    sleep(1)

    # BEGIN TRAINING
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_start")')

    # BEGINNER COURSE
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/ll_beginner")')

    # SETTINGS
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/settings")')

    # CREATE ACCOUNT
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_create_acc")')

    # Генерируем случайные значения для полей
    random_name = fake.first_name()
    random_email = fake.email()
    random_password = generate_random_password()

    # Заполняем поле Имя
    name = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Your name"]')
    name.send_keys(random_name)
    sleep(1)

    # Заполняем поле Email
    email = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Your email"]')
    email.send_keys(random_email)
    sleep(1)

    # Заполняем поле Password
    password = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Your password"]')
    password.send_keys(random_password)
    sleep(1)

    # SIGN UP
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_create_acc")')

    # Выбираем курс
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_course_old_price")')

    # SETTINGS
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/settings")')

    # QUIT
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Quit")')

