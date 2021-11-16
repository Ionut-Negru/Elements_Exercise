
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys


class Driver:
    
    def __init__(self):
        self.current_element = None
        self.driver_path = 'C:\\Users\\INegru\\Desktop\\chromedriver.exe'
        self.load_driver()
        
    def load_driver(self, driver_path= ''):
        if driver_path == '':
            self.browser = Chrome(self.driver_path)
        else:
            self.browser = Chrome(driver_path)
            
    def open_page(self, website=''):
        self.browser.get(website)
        self.browser.maximize_window()
    
    def close_page(self):
        self.browser.close()
        
        