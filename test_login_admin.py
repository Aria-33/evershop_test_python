from config import SeleniumBrowser
import time

def login_admin ():
    browser = SeleniumBrowser() #wait for the browser to be ready
    browser.open_page("http://localhost:8000/admin/login/")
    time.sleep(2)  # Wait for the page to load