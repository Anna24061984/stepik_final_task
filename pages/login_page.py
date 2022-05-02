from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By
import time

class LoginPage(BasePage):
    def should_be_login_url(self):
        assert "login" in self.url, "URL не содержит login"
        #assert "/login" in self.open(), "login is absent in current url"
        #assert self.browser.FindElement(By.CssSelector(*MainPageLocators.LOGIN_LINK)).GetAttribute("href").Contains("login"), "URL не содержит login"         
    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not presented"
        
    def register_new_user(self):
        self.go_to_login_page()
        email_str = str(time.time()) + "@fakemail.org"
        email = self.browser.find_element(*LoginPageLocators.EMAIL)
        email.send_keys(email_str)
        
        pswd_str = "gft56fgcGj.7"
        pswd = self.browser.find_element(*LoginPageLocators.PSWD)
        pswd.send_keys(pswd_str)
        
        pswd2 = self.browser.find_element(*LoginPageLocators.PSWD2)
        pswd2.send_keys(pswd_str)
        
        btn = self.browser.find_element(*LoginPageLocators.BTN_REG)
        btn.click()
                
        
        
       
      
   
   
   
    
    
