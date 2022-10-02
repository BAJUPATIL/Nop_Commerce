import time

import pytest

from selenium import webdriver
from pageObjects.LoginPage import LoginPage

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XlUtils


class Test_002_LDDT_ogin:
    baseUrl = ReadConfig.getApplicationURL()
    path = ".//TestData/testdata.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("********************** Test_002_DDT_Login **********************")

        self.logger.info("********************** Verifying Login Test **********************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)

        self.rows = XlUtils.getRowCount(self.path, 'Sheet1')
        print("number of rows in Excel...", self.rows)

        list_status = []

        for r in range(2, self.rows + 1):
            self.user = XlUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XlUtils.readData(self.path, 'Sheet1', r, 2)
            self.expt = XlUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            time.sleep(5)

            act_title = self.driver.title
            exp_title = 'Dashboard / nopCommerce administration'

            if act_title == exp_title:
                if self.expt == 'pass':
                    self.logger.info("************ Passed *********")
                    self.lp.clickLogout()
                    list_status.append('pass')
                elif self.expt=='fail':
                    self.logger.info("************ Failed *********")
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_LoginDDT_Test.png")
                    self.lp.clickLogout()

                    list_status.append('fail')


            elif act_title!=exp_title:
                if self.expt == 'pass':
                    self.logger.info("************ Failed *********")
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_LoginDDT_Test.png")

                    list_status.append('fail')
                elif self.expt=='fail':
                    self.logger.info("************ Passed *********")

                    list_status.append('pass')
            print(list_status)

        if 'fail' not in list_status:
            self.logger.info("***********Login DDT Test is Pass*************")
            self.driver.close()
            assert True
        else:
            self.logger.info("***********Login DDT Test Fail**********")
            self.driver.close()
            assert False

        self.logger.info('********** End oF DDT Test case **********')

        self.logger.info('********** End oF DDT Test case **********')


