from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_SECTION_IN_BASKET), \
            'Items section in the basket is not empty'
        empty_basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text.strip()
        assert empty_basket_text == 'Your basket is empty. Continue shopping', \
            '"Your basket is empty. Continue shopping" does not display'
