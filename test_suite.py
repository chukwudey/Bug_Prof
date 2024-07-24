import time

import pytest
from selenium import webdriver

from LoginPage.LoginPage_test import LoginPage
from NewCustomerPage.NewCustomerPage import NewCustomerPage
from SignoutPage.SignoutPage import SignOutPage


@pytest.fixture(scope="session")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.login_url("https://automationplayground.com/crm/login.html")
    return login_page


time.sleep(5)


def test_login_page(login):
    login.enter_email("chuks@gmail.com")
    login.enter_password("123456")
    login.enter_rememberme()
    login.enter_submit()


def test_new_customer_page_automation_play_ground(login):
    test_new_customer = NewCustomerPage(login.driver)
    test_new_customer.new_customer()
    test_new_customer.email("chuks@gmail.com")
    test_new_customer.firstname("Chuks")
    test_new_customer.lastname("julian")
    test_new_customer.city("Lagos")
    test_new_customer.state()
    test_new_customer.gender()
    test_new_customer.promotional_list()
    test_new_customer.submit()


def test_signOut_page(login):
    test_sign_out = SignOutPage(login.driver)
    test_sign_out.submit()
