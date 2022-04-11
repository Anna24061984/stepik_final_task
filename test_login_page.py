from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/accounts/login/" #login_link

def test_should_be_login_page(browser):       
    page = LoginPage(browser, link)
    page.open()    
    page.should_be_login_url()
    page.should_be_login_form()
    page.should_be_register_form()
   

    