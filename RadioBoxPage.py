
from Driver import *
from selenium.webdriver.common.action_chains import ActionChains

class RadioBoxPage(Driver):
    
    def __init__(self):
        super().__init__()
        self.open_page("https://demoqa.com/radio-button")
        self.get_elements()
        
    def get_labels(self):
        elements = self.browser.find_elements_by_xpath("//div[@class='container playgound-body']/div[@class='row']/div/div[1]/div/label")
        self.labels = []
        for i in elements:
            self.labels.append(i.text)
            
    def get_radio_buttons(self):
        elements = self.browser.find_elements_by_xpath("//div[@class='container playgound-body']/div[@class='row']/div/div[1]/div/input")
        self.radio_buttons = {}
        for i in range(len(self.labels)):
            self.radio_buttons[self.labels[i]] = elements[i]
            
    def get_elements(self):
        self.get_labels()
        self.get_radio_buttons()
        
    def select_option(self, option=''):
        self.current_option = option
        ActionChains(self.browser).click(self.radio_buttons[option]).perform()
        
    def get_result(self):
        try:
            element = self.browser.find_element_by_xpath("//div[@class='container playgound-body']/div[@class='row']/div/div[1]/p/span")
            return element.text
        except:
            return None
        