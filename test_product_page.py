from pages.main_page import MainPage
from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)           # инициализируем Page Object model для product page, задаем browser и link
    page.open()                                 # открываем product page
    page.add_to_basket()                        # добавляем товар в корзину
    page.solve_quiz_and_get_code()              # решаем задачку и используем ответ
    page.should_be_added_to_basket()            # проверяем корректность добавленного товара в корзину
    page.should_be_correct_price_in_basket()    # проверяем корректность цены добавленного товара в корзину
