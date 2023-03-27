from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest


@pytest.mark.parametrize('promo_link', ["promo=offer0", "promo=offer1", "promo=offer2", "promo=offer3", "promo=offer4",
                                        "promo=offer5", "promo=offer6",
                                        pytest.param("promo=offer7", marks=pytest.mark.xfail(reason="Wrong book name")),
                                        "promo=offer8", "promo=offer9"])
def test_guest_can_add_product_to_basket(browser, promo_link):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?{promo_link}'
    page = ProductPage(browser, link)           # иниц. Page Object model для product page, задаем browser и link
    page.open()                                 # открываем product page
    page.add_to_basket()                        # добавляем товар в корзину
    page.solve_quiz_and_get_code()              # решаем задачку и используем ответ
    page.should_be_added_to_basket()            # проверяем корректность добавленного товара в корзину
    page.should_be_correct_price_in_basket()    # проверяем корректность цены добавленного товара в корзину

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
    page = ProductPage(browser, link)       # иниц. Page Object model для product page, задаем browser и link
    page.open()                             # открываем product page
    page.add_to_basket()                    # добавляем товар в корзину
    page.should_not_be_success_message()    # не должно быть success message после добавления товара в корзину

def test_guest_cant_see_success_message(browser):
    link = 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
    page = ProductPage(browser, link)       # иниц. Page Object model для product page, задаем browser и link
    page.open()                             # открываем product page
    page.should_not_be_success_message()    # проверяем отсутствие success message если товар еще не в корзине

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
    page = ProductPage(browser, link)           # иниц. Page Object model для product page, задаем browser и link
    page.open()                                 # открываем product page
    page.add_to_basket()                        # добавляем товар в корзину
    page.should_success_message_disappear()     # success message должен пропасть со страницы

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_items_in_basket()
