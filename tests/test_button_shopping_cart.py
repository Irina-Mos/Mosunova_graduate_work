from turtledemo.penrose import start

import allure
import pytest
import time
from pages.page_main import MainPage

@allure.id("005")
@allure.label("Dodo")
@allure.title('Проверка работы кнопки "Корзина"')
@allure.description("Проверка открытия модального окна с корзиной заказа")
@pytest.mark.dodo_tests

def test_shopping_cart(driver):
    load_time = 0.0
    with allure.step('Открываем сайт "ДоДо".'):
        start_time = time.time()
        web = MainPage(driver)
        web.open()
        end_time = time.time()
        load_time = end_time - start_time

    allure.step(f"Страница загрузилась за: {load_time:.2f} сек.")

    with allure.step('Нажимаем на кнопку "Корзина".'):
        web.click_shp_cart()
        assert web.wait_shp_cart_modal(), "Модальное окно не открылось."


    with allure.step('Проверяем, что открылось модальное окно с корзиной заказа.'):
        assert web.wait_shp_cart_field(),"Поле c корзиной заказа не найдено."

    web.take_screenshot("Модальное окно корзины заказа.")
