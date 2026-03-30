import allure
import pytest
from pages.page_main import MainPage

@allure.id("005")
@allure.label("Dodo")
@allure.title('Проверка работы кнопки "Корзина"')
@allure.description("Проверка открытия модального окна с корзиной заказа")
@pytest.mark.dodo_tests
@pytest.mark.parametrize("driver", ["Edge", "Chrome"], indirect=True)
def test_shopping_cart(driver):
    with allure.step('Открываем сайт "ДоДо".'):
        web = MainPage(driver)
        web.open()


    with allure.step('Нажимаем на кнопку "Корзина".'):
        web.click_shp_cart()
        assert web.wait_shp_cart_modal(), "Модальное окно не открылось."


    with allure.step('Проверяем, что открылось модальное окно с корзиной заказа.'):
        assert web.wait_shp_cart_field(),"Поле c корзиной заказа не найдено."

    web.take_screenshot("Модальное окно корзины заказа.")
