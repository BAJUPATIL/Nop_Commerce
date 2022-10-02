from selenium.webdriver.common.by import By


class SearchCustomer:
    txtEmail = (By.ID, "SearchEmail")
    txtFirstName = (By.ID, "SearchFirstName")
    txtLastName = (By.ID, "SearchLastName")
    btnsearchId = (By.ID, "search-customers")

    tblSearchResults_xpath = (By.XPATH, "//table[@role='grid']")
    table_xpath = (By.XPATH, "//table[@id='customers-grid']")
    tableRows_xpath = (By.XPATH, "//table[@id='customers-grid']//tbody/tr")
    tableColumns_xpath = (By.XPATH, "//table[@id='customers-grid']//tbody/tr/td")

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(*SearchCustomer.txtEmail).clear()
        self.driver.find_element(*SearchCustomer.txtEmail).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element(*SearchCustomer.txtFirstName).clear()
        self.driver.find_element(*SearchCustomer.txtFirstName).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(*SearchCustomer.txtLastName).clear()
        self.driver.find_element(*SearchCustomer.txtLastName).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(*SearchCustomer.btnsearchId).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(*SearchCustomer.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(*SearchCustomer.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(*SearchCustomer.table_xpath)
            emailid = table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag


    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(*SearchCustomer.table_xpath)
            name = table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag