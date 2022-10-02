import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_searchCustomerByEmail_004:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerByEmail(self, setup):
        self.logger.info("***********Test_searchCustomerByEmail_004****")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***********Login Successful****")

        self.adcu = AddCustomer(self.driver)
        self.adcu.ClickOnCUstomerMenu()
        self.adcu.ClickOnCUstomerMenuItem()
        self.logger.info("******* Starting Search Customer By Email **********")

        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)

        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        self.driver.close()

        assert True == status

        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")
