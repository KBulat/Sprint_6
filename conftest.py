import pytest
from data import URLs
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(URLs.main_page)
    yield driver
    driver.quit()