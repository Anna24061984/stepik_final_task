from .pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('num', [*range(0,7), pytest.param(7, marks=pytest.mark.xfail), *range(8,10)])
def test_guest_can_add_product_to_basket(browser, num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
    page = ProductPage(browser, link)
    print(link)
    page.open()
    page.click_add_to_basket()
    page.check_name()    
    page.check_price()
    
    
    