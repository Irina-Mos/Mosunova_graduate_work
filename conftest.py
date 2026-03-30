import pytest
from selenium import webdriver
import time

@pytest.fixture()
def driver(request):
    b = request.param
    if b == "Edge":
        browser = webdriver.Edge()
    else:
        browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()