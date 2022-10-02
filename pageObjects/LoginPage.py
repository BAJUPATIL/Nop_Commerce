from selenium import webdriver

from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id = (By.ID, "Email")
    textbox_password_id = (By.ID,'Password')
    button_login_xpath = (By.XPATH,"//button[contains(text(),'Log in')]")
    button_logout_xpath=(By.XPATH,'//*[@id="navbarText"]/ul/li[3]/a')
    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        usr = self.driver.find_element(*LoginPage.textbox_username_id)
        usr.clear()
        usr.send_keys(username)

    def setPassword(self, password):
        usr = self.driver.find_element(*LoginPage.textbox_password_id)
        usr.clear()
        usr.send_keys(password)

    def clickLogin(self):
        self.driver.find_element(*LoginPage.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(*LoginPage.button_logout_xpath).click()