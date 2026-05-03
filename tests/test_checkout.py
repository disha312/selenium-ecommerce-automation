from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_flow(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Login
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Add item
    inventory_page.add_item_to_cart()
    inventory_page.go_to_cart()

    # Validate cart
    assert cart_page.get_product_name() == "Sauce Labs Backpack"

    # Checkout
    checkout_page.start_checkout()
    checkout_page.enter_details("John", "Doe", "12345")
    checkout_page.finish_order()

    # Validate success
    success_text = checkout_page.get_success_message()
    assert "Thank you for your order!" in success_text