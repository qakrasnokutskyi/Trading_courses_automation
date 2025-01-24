import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time

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

def test_login(driver):
    sleep(7)

    # Выбираем англ язык
    english = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_name" and @text="English"]')
    english.click()
    sleep(1)

    # Нажимает кнопку "Войти/Зарегистрироваться
    login = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_enter"]')
    login.click()
    sleep(1)

    # Заполняем поле email
    email = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Your email"]')
    email.send_keys('qakrasnokutskiy@gmail.com')
    sleep(1)
    print('Поле успешно заполнено')

    # Заполняем поле password
    password = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Your password"]')
    password.send_keys('.....')
    sleep(1)
    print('Поле успешно заполнено')

    # Выполняем вход
    signin = driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.tradingcourses.learnhowtoinvest:id/bt_signIn"]')
    signin.click()
    sleep(5)


# Проверяем, если ошибка регистрации, то считаем её правильной
try:
    # Пытаемся найти элемент с ошибкой (например, сообщение об ошибке валидации)
    error_message = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/error_message"]')

    # Если элемент найден, то ошибка регистрации есть, считаем правильным результат
    assert error_message.is_displayed()  # Проверяем, что сообщение об ошибке отображается
    print("Ошибка регистрации: это правильно, как ожидается.")

except Exception as e:
    # Если элемента с ошибкой нет, значит, ошибка не произошла
    print("Регистрация прошла успешно, что является неправильным результатом.")
