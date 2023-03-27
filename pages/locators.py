from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '.login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '.register_form')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ACTUAL_ITEM_NAME = (By.CSS_SELECTOR, '.product_main h1')
    ACTUAL_ITEM_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    ADDED_ITEM_NAME = (By.CSS_SELECTOR, '#messages .alert:first-child .alertinner strong')
    ADDED_ITEM_PRICE = (By.CSS_SELECTOR, '#messages .alert:nth-child(3) .alertinner strong')
