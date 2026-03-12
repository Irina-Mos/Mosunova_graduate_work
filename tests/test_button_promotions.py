import allure
import pytest
from pages.page_main import MainPage

@allure.id("004")
@allure.feature("Dodo")
@allure.label("Api test")
@allure.title('Проверка работы кнопки "Акции"')
@allure.description("Проверка открытия страницы с акциями")
@pytest.mark.dodo_tests


def test_promotions(driver):
    with allure.step('Открываем сайт "ДоДо".'):
        web = MainPage(driver)
        web.open()
    with allure.step('Проверка работы кнопки "Акции".'):
        web.select_promotions()
    with allure.step('Проверяем, что открылась страница с акциями.'):
        assert "bonusactions" in driver.current_url, "Переход на страницу с акциями не произошел."

