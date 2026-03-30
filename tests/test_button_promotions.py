import allure
import pytest
from pages.page_main import MainPage

@allure.id("004")
@allure.label("Dodo")
@allure.title('Проверка работы кнопки "Акции"')
@allure.description("Проверка открытия страницы с акциями")
@pytest.mark.dodo_tests
@pytest.mark.parametrize("driver", ["Edge", "Chrome"], indirect=True)
def test_promotions(driver):
    with allure.step('Открываем сайт "ДоДо".'):
        web = MainPage(driver)
        web.open()
    with allure.step('Нажимаем на кнопку "Акции".'):
        web.select_promotions()
    with allure.step('Проверяем, что открылась страница с акциями.'):
        assert "bonusactions" in driver.current_url, "Переход на страницу с акциями не произошел."

