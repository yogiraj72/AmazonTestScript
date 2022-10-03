import time
import pytest
from selenium import webdriver
from pageObjects.searchProduct import SearchProduct
from utilities.readConfig import ReadConfig
from utilities.customLogger import LogGen


# Test case for Amazon searchProduct
class TestCaseSearch:
    # Declare variable for test case
    baseURL = ReadConfig.getappurl()
    searchWord = ReadConfig.searchword()
    minValue = ReadConfig.minvalue()
    maxValue = ReadConfig.maxvalue()

    # initialized the looger class
    logger = LogGen.loggen()

    # Test case method to execute script
    def test_search_product(self, setup):

        self.logger.info("******* test_search_product *******")
        self.logger.info("******* Search Product on Amazon *******")

        # Browser up and search the amazon
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.logger.info("******* Click On Search Product on Amazon *******")
        self.search = SearchProduct(self.driver)
        self.logger.info("******* Search Samsung Product on Amazon Search Bar *******")
        self.search.searchbox("samsung")
        self.logger.info("******* Click Search Bar Button *******")
        self.search.searchbutton()
        self.logger.info("******* Filter Samsung Product on Amazon between 0 to 20000 *******")
        self.search.minprice("0")
        self.search.maxprice("20000")
        self.logger.info("******* Click On Filter Button *******")
        self.search.gofilter()
        self.logger.info("******* Select the Third Product in list *******")
        self.search.seleproduct()

        # Searching Product will Open in New Tab to handle it we use below method
        self.search.windowhandle()

        self.logger.info("******* Add the Selected product to Cart *******")
        self.search.addtocart()
        self.logger.info("******* Navigate to Cart *******")
        self.search.cartAdd()
        self.logger.info("******* Close the Browser *******")

        shop_title = self.driver.title
        if shop_title == 'Amazon.in Shopping Cart':
            assert True

        else:
            self.driver.save_screenshot(".\\screenShot\\" + "failTestCase.png")
            assert False

        self.driver.quit()













