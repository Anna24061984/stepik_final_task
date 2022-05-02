from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
login_url = "http://selenium1py.pythonanywhere.com"

@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.login_page = LoginPage(browser, login_url)            
        self.login_page.open()
        self.login_page.register_new_user()
        self.login_page.should_be_authorized_user()           
        
    def test_user_cant_see_success_message(self, browser): 
        self.page = ProductPage(browser, link)    
        self.page.open()                                 #Открываем страницу товара 
        self.page.should_not_be_success_message()        #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):        
        page = ProductPage(browser, link)    
        page.open()
        page.click_add_to_basket()
        page.check_name()    
        page.check_price()

@pytest.mark.need_review
@pytest.mark.parametrize('num', [*range(0,7), pytest.param(7, marks=pytest.mark.xfail), *range(8,10)])
def test_guest_can_add_product_to_basket(browser, num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'    
    page = ProductPage(browser, link)    
    page.open()    
    page.click_add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_name()    
    page.check_price()
    
@pytest.mark.need_review    
def ttest_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()    
    basket_page = BasketPage(browser, browser.current_url)    
    basket_page.should_be_message_about_empty()
    basket_page.should_be_empty_list_of_products()

@pytest.mark.need_review    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_url()
    login_page.should_be_login_form()
    
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    page = ProductPage(browser, link)    
    page.open()                     #Открываем страницу товара 
    page.click_add_to_basket()      #Добавляем товар в корзину     
    page.should_not_be_success_message()   

def test_message_disappeared_after_adding_product_to_basket(browser): 
    page = ProductPage(browser, link)    
    page.open()                     #Открываем страницу товара 
    page.click_add_to_basket()      #Добавляем товар в корзину
    page.should_disappear_success_message()  #Проверяем, что нет сообщения об успехе с помощью is_disappeared   
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

        
    