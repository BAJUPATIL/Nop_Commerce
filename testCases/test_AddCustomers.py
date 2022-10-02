import random
import string
import random
import pytest
import time
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from selenium.webdriver.common.by import By


class Test_003_AddCustomer:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("**********Test_003_AddCustomer***********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("********** Login... ***********")

        self.logger.info("********** Started Add Customer Test r***********")
        self.addcust=AddCustomer(self.driver)
        self.addcust.ClickOnCUstomerMenu()
        self.addcust.ClickOnCUstomerMenuItem()

        self.addcust.ClickOnAddNew()
        self.logger.info("********** Providing Customer Info ***********")

        self.email=random_generator() +"@gmail.com"

        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Pravin")
        self.addcust.setLastName("Kadam")
        self.addcust.setDOB("03/25/995") #mm/dd/yyy
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setCompanyName("BusyQA")
        self.addcust.setAdminContent("This is For Testing....")
        self.addcust.clikOnSave()

        self.logger.info("*********** Saving Customer Info **********")

        self.logger.info("*********** added customer validation started **********")

        self.msg=self.driver.find_element(By.TAG_NAME,"body").text

        print(self.msg)

        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("*********** Add Customer Case Is Passed **********")

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer.png")
            self.logger.info("*********** Add Customer Case Is Failed **********")
            assert False

        self.driver.close()
        self.logger.info("********Ending Add Customer Test********")















def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))