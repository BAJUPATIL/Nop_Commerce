import pytest

from selenium import webdriver
from pageObjects.LoginPage import LoginPage

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()


    @pytest.mark.regression
    def test_homePageTitle(self,setup):

        self.logger.info("********************** Testing Homepage Title **********************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        acttitle = self.driver.title

        if acttitle == 'Your store. Login':
            assert True
            self.logger.info("********************** Testing Homepage case id Passed **********************")

            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_HomePageTitle.png")
            self.driver.close()
            self.logger.error("********************** Testing Homepage case is Failed **********************")

            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.driver = setup
        self.logger.info("********************** Verifying Login Test **********************")

        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        acttitle = self.driver.title

        if acttitle == 'Dashboard / nopCommerce administration':
            self.driver.close()
            self.logger.info("********************** Verified Title After login **********************")

            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_HomePageTitle.png")
            self.driver.close()
            self.logger.error("********************** Login test case fail **********************")

            assert False
