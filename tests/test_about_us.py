import allure
import pytest
from pages.page_main import MainPage

@allure.id("008")
@allure.label("Dodo")
@allure.title('Проверка работы кнопки "О нас" в шапке сайта')
@allure.description("Проверка открытия страницы с информацией о сети пиццерий.")
@pytest.mark.dodo_tests

def test_about_us(driver):
    with allure.step('Открываем сайт "ДоДо".'):
        web = MainPage(driver)
        web.open()

    with allure.step('Нажимаем на кнопку "О нас".'):
        web.select_about_us()

    with allure.step('Проверяем, что открылась страница с информацией о сети пиццерий.'):
        assert "about" in driver.current_url, "Переход на страницу с информацией о сети пиццерий не произошел."