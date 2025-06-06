from config import SeleniumBrowser
import time

def login_admin ():
    browser = SeleniumBrowser() #attend que le navigateur soit prêt
    browser.open_page("http://localhost:8000/admin/login/")
    time.sleep(2)  # attend que la page se charge