
from Driver import *
from selenium.webdriver.common.action_chains import ActionChains

class RadioBoxPage(Driver):
    
    def __init__(self):
        super().__init__()
        self.open_page("https://demoqa.com/radio-button")
        self.get_elements()
        
    def get_elements(self):
        radio_buttons = self.browser.find_elements_by_xpath("//div[@class='container playgound-body']/div[@class='row']/div/div[1]/div/*[self::label or self::input]")
        self.labels = {}
        for i in range(0, len(radio_buttons), 2):
            label = radio_buttons[i+1].text
            btn = radio_buttons[i]
            self.labels[label] = btn
        
    def select_option(self, option=''):
        self.current_option = option
        ActionChains(self.browser).click(self.radio_buttons[option]).perform()
        
    def get_result(self):
        try:
            element = self.browser.find_element_by_xpath("//div[@class='container playgound-body']/div[@class='row']/div/div[1]/p/span")
            return element.text
        except:
            return None
        
        
        
""" Testing """

#aux = RadioBoxPage()
#for x in aux.labels:
#    print(x)
#aux.close_page()