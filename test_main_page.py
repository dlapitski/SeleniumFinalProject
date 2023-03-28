from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest

link = 'http://selenium1py.pythonanywhere.com/'


@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)  # иниц. Page Object для main_page
        page.open()                     # открываем страницу
        page.should_be_login_link()     # проверяем, что на странице есть логин линк

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)                          # иниц. Page Object для main_page
        page.open()                                             # открываем страницу
        page.go_to_login_page()                                 # переходим на login_page
        login_page = LoginPage(browser, browser.current_url)    # иниц. Page Object для login_page
        login_page.should_be_login_page()                       # проверяем присутствие правильных элементов


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)                          # иниц. Page Object для main_page
    page.open()                                             # открываем страницу
    page.go_to_basket_page()                                # переходим на basket_page
    basket_page = BasketPage(browser, browser.current_url)  # иниц. Page Object для basket_page
    basket_page.should_be_no_items_in_basket()              # проверяем отсутствие товаров в корзине
