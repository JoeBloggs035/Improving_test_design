from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        )
        add_to_basket_button.click()

    def expected_result1(self):
        self.should_be_product_added_message()
        self.assert_product_name()

    def should_be_product_added_message(self):
        assert self.is_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Product added message is not presented"

    def assert_product_name(self):
        # print("The added product is", self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET).text)
        # print("The product name is =", self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text)

        assert (
            self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
            == self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        ), "Product in the basket mismatch"

    def expected_result2(self):
        self.should_be_a_basket_price_message()
        self.assert_added_product_price_with_basket_price()

    def should_be_a_basket_price_message(self):
        assert self.is_element_present(
            *ProductPageLocators.BASKET_PRICE_MESSAGE
        ), "Basket price message is not presented"

    def assert_added_product_price_with_basket_price(self):
        # print("Added product price =", self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text)
        # print("Basket price =", self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text)
        assert (
            self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text
            == self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        ), "Price of product in the basket mismatch"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"