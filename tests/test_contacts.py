import allure
import pytest
from pages.page_main import MainPage

@allure.id("009")
@allure.label("Dodo")
@allure.title('Проверка работы кнопки "Контакты" в шапке сайта')
@allure.description("Проверка открытия страницы с информацией об адресах сети пиццерий.")
@pytest.mark.dodo_tests
@pytest.mark.parametrize("driver", ["Edge", "Chrome"], indirect=True)
def test_about_us(driver):
    with allure.step('Открываем сайт "ДоДо".'):
        web = MainPage(driver)
        web.open()

    with allure.step('Нажимаем на кнопку "Контакты".'):
        web.select_contacts()

    with allure.step('Проверяем, что открылась страница с информацией об адресах сети пиццерий.'):
        assert "contacts" in driver.current_url, "Переход на страницу с информацией об адресах сети пиццерий не произошел."