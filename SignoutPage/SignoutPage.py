import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from SignoutLocator.SignoutLocator_test import SigoutLacator


class SignOutPage:
    def __init__(self, driver):
        self.driver = driver

    def submit(self):
        click_submit = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(SigoutLacator.CLICK_SIGNOUT))
        click_submit.click()
        time.sleep(5)