import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddCustomer:
    lnkcustomermenu_xpath = (
        By.XPATH, "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]/p[1]")
    lnkcustomer_menuitem_path = (
        By.XPATH, "//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/p[1]")
    button_add_new_xpath = (By.XPATH, "/html/body/div[3]/div[1]/form[1]/div/div/a")
    input_email_xpath = (By.XPATH, "//input[@id='Email']")
    input_password_xpath = (By.XPATH, "//input[@id='Password']")
    input_firstName_xpath = (By.XPATH, "//input[@id='FirstName']")
    input_LastName_xpath = (By.XPATH, "//input[@id='LastName']")
    gender_male_id = (By.ID, 'Gender_Male')
    gender_femal_id = (By.ID, 'Gender_Female')

    input_DOB_xpath = (By.XPATH, "//input[@id='DateOfBirth']")

    input_CompanyName_xpath = (By.XPATH, "//input[@id='Company']")
    checkbox_is_Tax_xpath = (By.XPATH, "//input[@id='IsTaxExempt']")

    drop_NewsLetter_xpath = (By.XPATH,
                             "//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div[1]")
    customer_role_xpath = (By.XPATH,
                           "//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]")
    listite_admistrator_xpath = (By.XPATH, "//li[contains(text(),'Administrators')]")
    listite_forum_xpath = (By.XPATH, "//li[contains(text(),'Forum Moderators')]")
    listite_GUsts_xpath = (By.XPATH, "//li[contains(text(),'Guests')]")
    listite_registred_xpath = (By.XPATH, "//li[contains(text(),'Registered')]")
    listite_vendor_xpath = (By.XPATH, "//li[contains(text(),'Vendors')]")
    drmang_of_vendor = (By.XPATH, "//select[@id='VendorId']")
    checkactionbox = (By.XPATH, "//input[@id='Active']")
    input_admincomment_xpath = (By.XPATH, "//textarea[@id='AdminComment']")
    btn_save_xpath = (By.XPATH, "//body/div[3]/div[1]/form[1]/div[1]/div[1]/button[1]")

    def __init__(self, driver):
        self.driver = driver

    def ClickOnCUstomerMenu(self):
        self.driver.find_element(*AddCustomer.lnkcustomermenu_xpath).click()

    def ClickOnCUstomerMenuItem(self):
        self.driver.find_element(*AddCustomer.lnkcustomer_menuitem_path).click()

    def ClickOnAddNew(self):
        self.driver.find_element(*AddCustomer.button_add_new_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(*AddCustomer.input_email_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(*AddCustomer.input_password_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element(*AddCustomer.customer_role_xpath).click()

        time.sleep(3)
        if role == "Registered":
            self.listitem = self.driver.find_element(*AddCustomer.listite_registred_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element(*AddCustomer.listite_admistrator_xpath)
        elif role == "Guests":
            # user can select only registred or guests
            time.sleep(3)
            self.driver.find_element(By.XPATH, '//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[2]')
            self.listitem = self.driver.find_element(*AddCustomer.listite_GUsts_xpath)
        elif role == "Registered":
            self.listitem = self.driver.find_element(*AddCustomer.listite_registred_xpath)

        elif role == "Vendors":
            self.listitem = self.driver.find_element(*AddCustomer.listite_vendor_xpath)

        else:
            self.listitem = self.driver.find_element(*AddCustomer.listite_GUsts_xpath)
            time.sleep(3)
            self.driver.execute_script("argument[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(*AddCustomer.drmang_of_vendor))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(*AddCustomer.gender_male_id)

        elif gender == "Female":
            self.driver.find_element(*AddCustomer.gender_femal_id)

        else:
            self.driver.find_element(*AddCustomer.gender_male_id)

    def setFirstName(self, fname):
        self.driver.find_element(*AddCustomer.input_firstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(*AddCustomer.input_LastName_xpath).send_keys(lname)

    def setDOB(self, dob):
        self.driver.find_element(*AddCustomer.input_DOB_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(*AddCustomer.input_CompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(*AddCustomer.input_admincomment_xpath).send_keys(content)

    def clikOnSave(self):
        self.driver.find_element(*AddCustomer.btn_save_xpath).click()
