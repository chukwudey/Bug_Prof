import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from NewCustomerLocator.NewCustomerLocator_test import NewCustomerLOCATOR


class NewCustomerPage:
    def __init__(self, driver):
        self.driver = driver

    def new_customer(self):
        new_customer = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLOCATOR.CLICK_NEW_CUSTOMER))
        new_customer.click()

    def email(self, email):
        enter_email = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLOCATOR.ENTER_EMAIL))
        enter_email.send_keys(email)

    def firstname(self, firstname):
        enter_firstname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLOCATOR.ENTER_FIRSTNAME))
        enter_firstname.send_keys(firstname)

    def lastname(self, lastname):
        enter_lastname = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLOCATOR.ENTER_LASTNAME))
        enter_lastname.send_keys(lastname)

    def city(self, city):
        enter_city = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLOCATOR.ENTER_CITY)
        )
        enter_city.send_keys(city)
        time.sleep(10)

    def state(self):
        click_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLOCATOR.CLICK_STATE_DROP_DOWN))
        click_state.click()
        time.sleep(5)

    def select_state(self):
        click_select_state = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLOCATOR.SELECT_STATE))
        click_select_state.click()
        time.sleep(5)

    def gender(self):
        click_gender = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLOCATOR.ENTER_GENDER))
        click_gender.click()

    def promotional_list(self):
        click_promotional_list = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLOCATOR.PROMOTIONAL_LIST))
        click_promotional_list.click()

    def submit(self):
        click_submit = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(NewCustomerLOCATOR.SUBMIT)
        )
        click_submit.click()
        time.sleep(5)
