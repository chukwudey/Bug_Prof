import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from LoginLocator.LoginLocator_test import LoginLocatorPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        enter_email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocatorPage.USERNAME))
        enter_email.send_keys(email)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocatorPage.PASSWORD))
        enter_password.send_keys(password)

    def enter_rememberme(self):
        enter_rememberme = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocatorPage.REMEMBER))
        enter_rememberme.click()

    def enter_submit(self):
        enter_submit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocatorPage.SUBMIT))
        enter_submit.click()
        time.sleep(5)
