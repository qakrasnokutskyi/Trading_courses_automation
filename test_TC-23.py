import pytest
from appium import webdriver
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

def test_change_language(driver):
    sleep(7)

    # Выбираем англ язык
    english = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_name" and @text="English"]')
    english.click()
    sleep(1)

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
    element = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout')
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
    start_x = size['width'] * 0.2  # Начальная точка (80% от ширины экрана)
    end_x = size['width'] * 0.8  # Конечная точка (20% от ширины экрана)
    start_y = size['height'] / 2  # Центр экрана по высоте

    # Свайп с использованием метода swipe() (если используется более старая версия Appium)
    driver.swipe(start_x, start_y, end_x, start_y, 1000)  # Время свайпа - 1000 миллисекунд
    sleep(1)

# Получаем координаты элементов для свайпа
    element = driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout')
    size = driver.get_window_size()

    # Начальные и конечные координаты для свайпа влево
    start_x = size['width'] * 0.2  # Начальная точка (80% от ширины экрана)
    end_x = size['width'] * 0.8  # Конечная точка (20% от ширины экрана)
    start_y = size['height'] / 2  # Центр экрана по высоте

    # Свайп с использованием метода swipe() (если используется более старая версия Appium)
    driver.swipe(start_x, start_y, end_x, start_y, 1000)  # Время свайпа - 1000 миллисекунд
    sleep(1)

    # Получаем координаты элементов для свайпа
    element = driver.find_element(By.XPATH,
                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout')
    size = driver.get_window_size()

    # Начальные и конечные координаты для свайпа влево
    start_x = size['width'] * 0.2  # Начальная точка (80% от ширины экрана)
    end_x = size['width'] * 0.8  # Конечная точка (20% от ширины экрана)
    start_y = size['height'] / 2  # Центр экрана по высоте

    # Свайп с использованием метода swipe() (если используется более старая версия Appium)
    driver.swipe(start_x, start_y, end_x, start_y, 1000)  # Время свайпа - 1000 миллисекунд
    sleep(1)

    #Нажимаем кнопку "BEGIN TRAINING"
    start_button = driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button')
    start_button.click()
    sleep(5)

    #Выбираем "Про+ курс"
    advancedPRO = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]')
    advancedPRO.click()
    sleep(5)

    #Переходим в создать аккаунт
    settings = driver.find_element(By.XPATH,'//android.widget.FrameLayout[@content-desc="Settings"]/android.widget.FrameLayout/android.widget.ImageView')
    settings.click()
    sleep(3)

    tap_create_account = driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.ScrollView/android.view.ViewGroup/android.widget.Button')
    tap_create_account.click()
    sleep(3)

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

    # Заходим в новый аккаунт
    signup = driver.find_element(By.XPATH,'//android.widget.Button[@resource-id="com.tradingcourses.learnhowtoinvest:id/bt_signIn"]')
    signup.click()
    sleep(5)

    #Выбираем начальный курс
    begginer = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]')
    begginer.click()
    sleep(2)

    # Переходим в раздел "Обучение" для смены курса
    training = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="Training"]/android.widget.FrameLayout/android.widget.ImageView')
    training.click()
    sleep(2)

    # Выбираем новый курс
    change_course = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button')
    change_course.click()
    sleep(2)

    beginner = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]')
    beginner.click()
    sleep(2)

    change_course = driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button')
    change_course.click()
    sleep(2)

    intermediate = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]')
    intermediate.click()
    sleep(2)

    change_course = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button')
    change_course.click()
    sleep(2)

    advanced = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]')
    advanced.click()
    sleep(2)

    change_course = driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button')
    change_course.click()
    sleep(2)

    advancedPRO = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]')
    advancedPRO.click()
    sleep(5)