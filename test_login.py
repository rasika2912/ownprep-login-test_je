import pytest
from selenium import webdriver
from test_login_dropdown import LoginPage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_valid_login(setup):
    login = LoginPage(setup)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    assert "inventory" in setup.current_url  

def test_invalid_login(setup):
    login = LoginPage(setup)
    login.enter_username("wrong_user")
    login.enter_password("wrong_pass")
    login.click_login()

    error = login.get_error()
    assert "Username and password do not match" in error  
