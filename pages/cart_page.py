from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, driver):
        self.driver = driver

        self.product_name = (By.CLASS_NAME, "inventory_item_name")

    def get_product_name(self):
        return self.driver.find_element(*self.product_name).text