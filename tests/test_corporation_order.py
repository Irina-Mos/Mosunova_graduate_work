import allure
import pytest
from pages.page_main import MainPage

@allure.id("010")
@allure.label("Dodo")
@allure.title('Проверка работы кнопки "Корпоративные заказы"')
@allure.description("Проверка открытия модального окна с созданием корпоративного профиля.")
@pytest.mark.dodo_tests

def test_corp_order(driver):
    with allure.step('Открываем сайт "ДоДо".'):
        web = MainPage(driver)
        web.open()

    with allure.step('Нажимаем на кнопку "Корпоративные заказы".Проверяем, что открылось модальное окно с созданием корпоративного профиля.'):
        web.select_corporate_orders()
        assert web.wait_corporate_order_modal(), "Модальное окно не открылось."

    web.take_screenshot("Модальное окно с созданием корпоративного профиля.")