import allure
import pytest
from pages.page_main import MainPage

@allure.id("003")
@allure.feature("Dodo")
@allure.label("Api test")
@allure.title('Проверка работы кнопки "Войти"')
@allure.description("Проверка открытия модального окна с авторизацией по номеру телефона")
@pytest.mark.dodo_tests

def test_login(driver):
    with allure.step('Открываем сайт "ДоДо".'):
        web = MainPage(driver)
        web.open()
    with allure.step('Нажимаем на кнопку "Войти".'):
        web.click_login()
        assert web.wait_login_modal(), "Модальное окно не открылось."

    with allure.step('Проверяем, что открылось модальное окно ввода телефона.'):
        assert web.wait_phone_field(), "Поле ввода телефона не найдено."

    web.take_screenshot("Модальное окно авторизации.")
