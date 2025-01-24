import pytest
from appium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep, time
from faker import Faker
import random
import string

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
        android_driver.quit()


def rotate_screen(driver, orientation):
    # orientation: 'LANDSCAPE' or 'PORTRAIT'
    driver.orientation = orientation

#=============================================#


def test_registration(driver):
    sleep(7)

    # Выбираем англ язык
    english = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_name" and @text="English"]')
    english.click()
    sleep(1)

    # Нажимает кнопку "Войти/Зарегистрироваться
    login = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_enter"]')
    login.click()
    sleep(1)

    # Переходим в раздел "Регистрация"
    registration = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_tab_reg"]')
    registration.click()
    sleep(1)



    # Заполняем поле Имя
    name = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Your name"]')
    name.send_keys('')
    sleep(1)

    # Заполняем поле Email
    email = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Your email"]')
    email.send_keys('')
    sleep(1)

    # Заполняем поле Password
    password = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Your password"]')
    password.send_keys('')
    sleep(1)

    # Заходим в новый аккаунт
    signup = driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.tradingcourses.learnhowtoinvest:id/bt_signIn"]')
    signup.click()
    sleep(5)

    # Проверяем, если элемент "beginner" отобразился
    try:
        # Пытаемся найти элемент с "beginner"
        beginner = driver.find_element(By.XPATH,'//android.view.ViewGroup[@resource-id="com.tradingcourses.learnhowtoinvest:id/ll_beginner"]')

        # Если элемент найден, значит, тест должен падать
        if beginner.is_displayed():
            print("Элемент 'beginner' отобразился! Тест не пройден.")
            assert False  # Это приведет к падению теста
    except NoSuchElementException:
        # Если элемента нет (ошибка поиска), то тест считается положительным
        print("Элемент 'beginner' не отобразился. Тест положительный.")