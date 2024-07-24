from selenium.webdriver.common.by import By


class LoginLocatorPage:
    USERNAME = (By.ID, "email-id")
    PASSWORD = (By.ID, "password")
    REMEMBER = (By.ID, "remember")
    SUBMIT = (By.ID, "submit-id")
