from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_add_item_to_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # Login
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Add item
    inventory_page.add_item_to_cart()
    inventory_page.go_to_cart()

    # Validate product
    product = cart_page.get_product_name()
    assert product == "Sauce Labs Backpack"