import math
from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_added_to_basket(self):
        actual_item_name = self.browser.find_element(*ProductPageLocators.ACTUAL_ITEM_NAME).text
        expected_item_name = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_NAME).text
        assert expected_item_name == actual_item_name, 'Book name is different'

    def should_be_correct_price_in_basket(self):
        actual_item_price = self.browser.find_element(*ProductPageLocators.ACTUAL_ITEM_PRICE).text
        expected_item_price = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_PRICE).text
        assert expected_item_price == actual_item_price, 'Book price is different'
