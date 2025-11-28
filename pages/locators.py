from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form.well")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form.well")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (
        By.CSS_SELECTOR,
        ".btn.btn-lg.btn-primary.btn-add-to-basket",
    )
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    ADDED_PRODUCT_NAME = (
        By.CSS_SELECTOR,
        "#messages .alert-success:first-child strong",
    )
    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        "#messages .alert-success:first-child .alertinner",
    )
    BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner p strong")
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main p.price_color")
