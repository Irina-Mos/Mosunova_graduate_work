import allure
import pytest
from pages.page_main import MainPage

@allure.id("006")
@allure.label("Dodo")
@allure.title('Проверка работы кнопки "Прямой эфир" в шапке сайта')
@allure.description("Проверка запуска видео прямого эфира с кухни одного из филиалов сети пиццерий.")
@pytest.mark.dodo_tests

def test_live_broadcast(driver):
    with allure.step('Открываем сайт "ДоДо".'):
        web = MainPage(driver)
        web.open()

    with allure.step('Проверка работы кнопки "Прямой эфир".'):
        web.click_live_broadcast_button()
        assert web.wait_live_broadcast(), "Прямой эфир не отображается"
