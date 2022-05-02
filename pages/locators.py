from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
        
class LoginPageLocators():    
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR,".register_form input[name='registration-email']")
    PSWD = (By.CSS_SELECTOR,".register_form input[name='registration-password1']")
    PSWD2 = (By.CSS_SELECTOR,".register_form input[name='registration-password2']")
    BTN_REG = (By.CSS_SELECTOR, "button[name='registration_submit']")
    
class ProductPageLocators():
    ADD_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADD_BOOK_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    ADD_BOOK_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc") 
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")    
    
class BasketPageLocators():
    BASKET_BTN = (By.CSS_SELECTOR, "span a.btn-default")    
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "div#content_inner>p")
    ANY_PRODUCT = (By.CSS_SELECTOR, "basket-title")
    
    