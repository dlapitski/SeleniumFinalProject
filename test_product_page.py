from pages.product_page import ProductPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from random import randrange as rr
import pytest


link_to_product1 = 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
link_to_product2 = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'


@pytest.mark.need_review
@pytest.mark.parametrize('promo_link', ["promo=offer0", "promo=offer1", "promo=offer2", "promo=offer3", "promo=offer4",
                                        "promo=offer5", "promo=offer6",
                                        pytest.param("promo=offer7", marks=pytest.mark.xfail(reason="Wrong book name")),
                                        "promo=offer8", "promo=offer9"])
def test_guest_can_add_product_to_basket(browser, promo_link):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?{promo_link}'
    page = ProductPage(browser, link)           # иниц. Page Object для product_page
    page.open()                                 # открываем product_page
    page.add_to_basket()                        # добавляем товар в корзину
    page.solve_quiz_and_get_code()              # решаем задачку и используем ответ
    page.should_be_added_to_basket()            # проверяем корректность добавленного товара в корзину
    page.should_be_correct_price_in_basket()    # проверяем корректность цены добавленного товара в корзину


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_to_product1)   # иниц. Page Object для product_page
    page.open()                                     # открываем product_page
    page.add_to_basket()                            # добавляем товар в корзину
    page.should_not_be_success_message()            # проверяем отсутствие success message


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link_to_product1)   # иниц. Page Object для product_page
    page.open()                                     # открываем product_page
    page.should_not_be_success_message()            # проверяем отсутствие success message если товар еще не в корзине


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_to_product1)   # иниц. Page Object для product_page
    page.open()                                     # открываем product_page
    page.add_to_basket()                            # добавляем товар в корзину
    page.should_success_message_disappear()         # success message должен пропасть со страницы


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link_to_product2)   # иниц. Page Object для product_page
    page.open()                                     # открываем product_page
    page.should_be_login_link()                     # проверяем наличие login link


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link_to_product2)           # иниц. Page Object для product_page
    page.open()                                             # открываем product_page
    page.go_to_login_page()                                 # переходим на login_page
    login_page = LoginPage(browser, browser.current_url)    # иниц. Page Object для login_page
    login_page.should_be_login_page()                       # проверяем наличие login link


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link_to_product2)           # иниц. Page Object для product_page
    page.open()                                             # открываем product_page
    page.go_to_basket_page()                                # переходим на basket_page
    basket_page = BasketPage(browser, browser.current_url)  # иниц. Page Object для basket_page
    basket_page.should_be_no_items_in_basket()              # проверяем отсутствие товаров в корзине


@pytest.mark.logged_in_user
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/'
        main_page = MainPage(browser, link)                                     # иниц. Page Object для main_page
        main_page.open()                                                        # открываем main_page
        main_page.go_to_login_page()                                            # переходим на login_page
        login_page = LoginPage(browser, browser.current_url)                    # иниц. Page Object для login_page
        login_page.register_new_user(
            email=f'email+{rr(1, 100000)}@example.com', password='Test1234!')   # регистрируем нового юзера
        main_page.should_be_authorized_user()                                   # проверяем авторизацию юзера

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link_to_product1)   # иниц. Page Object для product_page
        page.open()                                     # открываем product_page
        page.should_not_be_success_message()            # проверяем отсутствие success message

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        page = ProductPage(browser, link)           # иниц. Page Object для product_page
        page.open()                                 # открываем product_page
        page.add_to_basket()                        # добавляем товар в корзину
        page.solve_quiz_and_get_code()              # решаем задачку и используем ответ
        page.should_be_added_to_basket()            # проверяем корректность добавленного товара в корзину
        page.should_be_correct_price_in_basket()    # проверяем корректность цены добавленного товара в корзину
