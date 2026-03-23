import allure
import pytest
from pages.page_main import MainPage

@allure.id("002")
@allure.label("Dodo")
@allure.title('Проверка работы кнопки "Додокоины"')
@allure.description("Проверка открытия страницы с программой лояльности")
@pytest.mark.dodo_tests


def test_dodocoins(driver):
    with allure.step('Открываем сайт "ДоДо".'):
        web = MainPage(driver)
        web.open()
    with allure.step('Нажимаем на кнопку "Додокоины".'):
        web.select_dodocoins()
    with allure.step('Проверяем, что открылась страница программы лояльности.'):
        assert "loyaltyprogram" in driver.current_url, "Переход на страницу лояльности не произошёл."

