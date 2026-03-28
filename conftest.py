import pytest
from selenium import webdriver
import time

@pytest.fixture()
def driver():
    chrome = webdriver.Firefox()
    chrome.maximize_window()
    chrome.implicitly_wait(10)
    yield chrome
    chrome.quit()