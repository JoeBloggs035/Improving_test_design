# pytest -vs --tb=line --browser_name=firefox --language=fr test_product_page.py
import time

from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()
    time.sleep(2) # специально для firefox
    product_page.expected_result1()
    product_page.expected_result2()
