from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest

link = 'http://selenium1py.pythonanywhere.com/'


@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                     # открываем страницу
        page.should_be_login_link()     # выполняем метод страницы - проверяем, что на странице есть логин линк

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)      # инициализируем Page Object для main_page, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                         # открываем страницу
        page.go_to_login_page()             # переходим на login page
        login_page = LoginPage(browser, browser.current_url)  # инициализируем Page Object для login_page, передаем в контруктор экземпляр драйвера и url адрес
        login_page.should_be_login_page()   # выполняем метод страницы - проверяем присутствие правильных элементов


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_items_in_basket()
