import time
import allure
import pytest
from selenium.webdriver.common.by import By

def test_login(driver):
    with allure.step('Открываем сайт "ДоДо".'):
        driver.get("https://dodopizza.ru/perm")
    with allure.step('Нажимаем на кнопку "Войти".'):
        login = driver.find_element(By.XPATH, "//button[@class='sc-18x94tv-0 hNSEqk']")
        login.click()
        time.sleep(3)
        modal = driver.find_element(By.XPATH, "//div[@class='sc-1ne9bn6-0 eOsDZW sc-17puf9f-0 bWXvcs']")
        assert modal.is_displayed(), "Модальное окно не открылось."

    with allure.step('Проверяем, что открылось модальное окно ввода телефона.'):
        phone_field = driver.find_element(By.XPATH,"//div[@class='sc-8yov1q-0 gFACJZ']")
        assert phone_field.is_displayed(), "Поле ввода телефона не найдено."

    allure.attach(
        driver.get_screenshot_as_png(),
        name= "Модальное окно авторизации.",
        attachment_type=allure.attachment_type.PNG
        )