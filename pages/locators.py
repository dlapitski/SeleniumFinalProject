from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_invalid')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '.login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '.register_form')
    EMAIL = (By.NAME, 'registration-email')
    PASSWORD = (By.NAME, 'registration-password1')
    CONFIRM_PASSWORD = (By.NAME, 'registration-password2')
    REGISTER_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ACTUAL_ITEM_NAME = (By.CSS_SELECTOR, '.product_main h1')
    ACTUAL_ITEM_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    ADDED_ITEM_NAME = (By.CSS_SELECTOR, '#messages .alert:first-child .alertinner strong')
    ADDED_ITEM_PRICE = (By.CSS_SELECTOR, '#messages .alert:nth-child(3) .alertinner strong')
    SUCCESS_MESSAGE1 = (By.CSS_SELECTOR, '#messages .alert-success:nth-child(1)')
    SUCCESS_MESSAGE2 = (By.CSS_SELECTOR, '#messages .alert-success:nth-child(2)')


class BasketPageLocators:
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini .btn-group > [href*="basket"]')
    ITEMS_SECTION_IN_BASKET = (By.CSS_SELECTOR, '.basket_summary')
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, '#content_inner p')
