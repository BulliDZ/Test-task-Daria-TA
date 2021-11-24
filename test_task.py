import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://rozetka.com.ua/"


def test_contact():
    try:
        # Arrange
        browser = webdriver.Chrome('C:\\Your\\path\\to\\your chromedriver\\chromedriver.exe')
        browser.maximize_window()
        browser.implicitly_wait(10)
        browser.get(link)

        # Act

        # Write your code here

        # Assert

        # Write your asserts here
        assert 1
    finally:
        browser.quit()
