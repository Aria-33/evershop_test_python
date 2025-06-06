from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class SeleniumBrowser:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(), options=chrome_options)
# # Initialise le navigateur Chrome avec les options par défaut.
#       
#       Exemple d'utilisation :
#            browser = SeleniumBrowser()
##

    def open_page(self, url):
        self.driver.get(url)
# # Ouvre la page web à l'URL spécifiée.
#   
#       Exemple d'utilisation :
#           browser.open_page("https://www.example.com")
# #