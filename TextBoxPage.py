
from Driver import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class TextBoxPage(Driver):
    
    def __init__(self):
        super().__init__()
        self.label_xpath = "//div[@class='text-field-container']/form[@id='userForm']/div/div/label"
        self.text_boxs_xpath = "//div[@class='text-field-container']/form[@id='userForm']/div/div/*[self::input or self::textarea]"
        self.submit_xpath = "//form[@id='userForm']/div/div/button[@id='submit']"
        self.inputs = {}
        
    def set_label_xpath(self, xpath=''):
        self.label_xpath = xpath
    
    def set_submit_button_xpath(self, xpath=''):
        self.submit_xpath = xpath
    
    def set_text_boxs_xpath(self, xpath=''):
        self.text_boxs_xpath = xpath
    
    def get_labels(self):
        elements = self.browser.find_elements_by_xpath(self.label_xpath)
        self.labels = []
        for aux in elements:
            self.labels.append(aux.text)
    
    def get_text_boxs(self):
        elements = self.browser.find_elements_by_xpath(self.text_boxs_xpath)
        self.form = {}
        for i in range(len(self.labels)):
            self.form[self.labels[i]] = elements[i]
    
    def load_form_elements(self):
        self.get_labels()
        self.get_text_boxs()
            
    def insert_text(self, target='', text=''):
        self.inputs[target] = text
        self.form[target].send_keys(text)
    
    def submit_form(self):
        button = self.browser.find_element_by_xpath(self.submit_xpath)
        try:
            button.click()
        except:
            ActionChains(self.browser).move_to_element(button).send_keys(Keys.PAGE_DOWN).move_to_element(button).perform()
            button.click()
        
    def get_results(self):
        aux = self.browser.find_elements_by_xpath("//form[@id='userForm']/div[@id='output']/div/p")
        self.results = {}
        for i in range(len(self.labels)):
            self.results[self.labels[i]] = aux[i].text.split(":")[1]
    
    def insert_text_in_all(*args):
        for i in range(1,len(args)):
            args[0].insert_text(args[0].labels[i-1],args[i])
        
    def get_result_by_name(self, name=''):
        return self.results[name]
