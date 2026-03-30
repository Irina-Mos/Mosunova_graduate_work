import allure
import pytest
from pages.page_main import MainPage

@allure.id("007")
@allure.label("Dodo")
@allure.title('Проверка работы кнопки "Работа в Додо" в шапке сайта')
@allure.description("Проверка открытия страницы с вакансиями.")
@pytest.mark.dodo_tests
@pytest.mark.parametrize("driver", ["Edge", "Chrome"], indirect=True)
def test_work(driver):
    with allure.step('Открываем сайт "ДоДо".'):
        web = MainPage(driver)
        web.open()

    with allure.step('Нажимаем на кнопку "Работа в Додо".'):
        web.select_work_in_dodo()

    with allure.step('Переключение на окно "Работа в Додо".'):
        web.select_window(1)

    with allure.step('Проверяем, что открылась страница с вакансиями.'):
        assert "rabotavdodo" in driver.current_url, "Переход на страницу с вакансиями не произошел."