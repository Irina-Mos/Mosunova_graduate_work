import allure
import pytest
from pages.page_main import MainPage


@allure.id("001")
@allure.label("Dodo")
@allure.title("Переключение между вкладками")
@allure.description("Проверка переключения между основными вкладками меню сайта")
@pytest.mark.dodo_tests

def test_tabs(driver):
    with allure.step('Открываем сайт "ДоДо".'):
        web = MainPage(driver)
        web.open()
    with allure.step('Проверка переключения между вкладками.'):
        web.scroll_to_combo()
        pass
        # web.check_tabs()

