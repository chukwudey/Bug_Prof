from selenium.webdriver.common.by import By


class NewCustomerLOCATOR:
    CLICK_NEW_CUSTOMER = (By.ID, "new-customer")
    ENTER_EMAIL = (By.ID, "EmailAddress")
    ENTER_FIRSTNAME = (By.ID, "FirstName")
    ENTER_LASTNAME = (By.ID, "LastName")
    ENTER_CITY = (By.ID, "City")
    CLICK_STATE_DROP_DOWN = (By.ID, "StateOrRegion")
    SELECT_STATE = (By.XPATH, '//*[@id="StateOrRegion"]/option[7]')
    ENTER_GENDER = (By.XPATH, '//*[@id="loginform"]/div/div/div/div/form/div[6]/input[1]')
    PROMOTIONAL_LIST = (By.XPATH, '//*[@id="loginform"]/div/div/div/div/form/div[7]/input')
    SUBMIT = (By.XPATH, '//*[@id="loginform"]/div/div/div/div/form/button')
