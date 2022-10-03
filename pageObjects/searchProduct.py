from selenium.webdriver.common import window
from selenium.webdriver.common.keys import Keys


# This class is of amazon page
class SearchProduct:

    # All the webelement located using xpath required the script

    search_box_id = "//input[@id='twotabsearchtextbox']"
    search_btn_id = "//input[@id='nav-search-submit-button']"
    min_price = "//input[@id='low-price']"
    max_price = "//input[@id='high-price']"
    go_filter = "//input[@class='a-button-input']"
    select_product = "//div[@data-index='4']//a[@class='a-link-normal s-no-outline']"
    add_to_cart = "//input[@id='add-to-cart-button']"
    cart = "//div[@id='attach-accessory-pane']//form//input"


    # initialized the driver

    def __init__(self, driver):
        self.driver = driver

    # Methods for all webelements locator

    def searchbox(self, searchword):
        self.driver.find_element("xpath", self.search_box_id).send_keys(searchword)

    def searchbutton(self):
        btn_click = self.driver.find_element("xpath", self.search_btn_id)
        btn_click.send_keys(Keys.ENTER)

    def minprice(self, minprice):
        self.driver.find_element("xpath", self.min_price).send_keys(minprice)

    def maxprice(self, maxprice):
        self.driver.find_element("xpath", self.max_price).send_keys(maxprice)

    def gofilter(self):
        go_fil = self.driver.find_element("xpath", self.go_filter)
        go_fil.click()

    def seleproduct(self):
        self.driver.find_element("xpath", self.select_product).click()

    def addtocart(self):
        add_to = self.driver.find_element("xpath", self.add_to_cart)
        add_to.click()

    def windowhandle(self):
        child_page = self.driver.window_handles[1]
        self.driver.switch_to.window(child_page)

    def cartAdd(self):
        self.driver.find_element("xpath", self.cart).click()










