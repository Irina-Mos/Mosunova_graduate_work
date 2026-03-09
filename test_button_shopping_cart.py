import time
import allure
import pytest
from selenium.webdriver.common.by import By

def test_shopping_cart(driver):
    with allure.step('Открываем сайт "ДоДо".'):
        driver.get("https://dodopizza.ru/perm")
    with allure.step('Нажимаем на кнопку "Корзина".'):
        shp_cart = driver.find_element(By.XPATH, "//button[@class='sc-18x94tv-0 hNSEqk sc-1uavg9b-11 eETFSt']")
        shp_cart.click()
        time.sleep(3)
        modal = driver.find_element(By.XPATH, "//main[@class='sc-1gxjiqu-0 dqtuND']")
        assert modal.is_displayed(), "Модальное окно не открылось."

    with allure.step('Проверяем, что открылось модальное окно с корзиной заказа.'):
        shp_cart_field = driver.find_element(By.XPATH,"//button[@class='button-close']")
        assert shp_cart_field.is_displayed(), "Поле c корзиной заказа не найдено."

    allure.attach(
        driver.get_screenshot_as_png(),
        name= "Модальное окно корзины заказа.",
        attachment_type=allure.attachment_type.PNG
        )