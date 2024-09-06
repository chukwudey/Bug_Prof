import time

import pytest
from selenium import webdriver

from LoginPage.LoginPage_test import LoginPage
from NewCustomerPage.NewCustomerPage import NewCustomerPage
from SignoutPage.SignoutPage import SignOutPage
from config.config import Config, ConfigNewCustomer


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
    login_page.login_url(Config.URL)
    return login_page


time.sleep(5)


def test_login_page(login):
    login.enter_email(Config.UserName)
    login.enter_password(Config.Password)
    login.enter_rememberme()
    login.enter_submit()


def test_new_customer_page_automation_play_ground(login):
    test_new_customer = NewCustomerPage(login.driver)
    test_new_customer.new_customer()
    test_new_customer.email(ConfigNewCustomer.Email)
    test_new_customer.firstname(ConfigNewCustomer.Firstname)
    test_new_customer.lastname(ConfigNewCustomer.Lastname)
    test_new_customer.city(ConfigNewCustomer.City)
    test_new_customer.state()
    test_new_customer.gender()
    test_new_customer.promotional_list()
    test_new_customer.submit()


def test_signOut_page(login):
    test_sign_out = SignOutPage(login.driver)
    test_sign_out.submit()
