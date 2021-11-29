
from Driver import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class TextBoxPage(Driver):
    
    def __init__(self):
        super().__init__()
        self.submit_xpath = "//form[@id='userForm']/div/div/button[@id='submit']"
        self.inputs = {}
        self.wrappers_xpath = "//div[@class='text-field-container']/form[@id='userForm']/div[contains(@id,'wrapper')]"
        self.open_page()
        
    def open_page(self):
        self.browser.get("http://demoqa.com/text-box")
        self.browser.maximize_window()
    
    def collect_from_wrappers(self):
        element = self.browser.find_elements_by_xpath(self.wrappers_xpath)
        self.labels = {}
        i = 0
        for aux in element:
            label = 'placeholder'+str(i)
            we = ''
            try:
                we = aux.find_element_by_xpath(".//*[self::input or self::textarea]")
                label = aux.find_element_by_xpath(".//label").text.lower().replace(' ','_')
            except:
                i = i + 1
            finally:
                self.labels[label] = we
        return self.labels
        
    def set_wrappers_xpath(self, xpath=''):
        self.wrappers_xpath = xpath
    
    def set_submit_button_xpath(self, xpath=''):
        self.submit_xpath = xpath
            
    def insert_text(self, target='', text=''):
        self.labels[target].clear()
        self.labels[target].send_keys(text)
        
    
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
        for x in aux:
            self.results[x.text.split(":")[0]] = x.text.split(":")[1]
            
    def get_insert_keywords(self):
        """
            Returns a list of the current available keywords for the insert method
        """
        aux = []
        for x in self.labels:
            aux.append(x)
        return aux
    
    def insert_text_in_all(self,**kwargs):
        """
            Takes any number of keyword arguments
            Will insert the values passed into the textboxs of the form
            To see the current keywords option use get_insert_keywords
        """
        for x in kwargs:
            try:
                self.insert_text(x, kwargs[x])
            except:
                print(f'There is no label named : {x}')
        self.submit_form()
        
    def get_result_by_name(self, name=''):
        return self.results[name]


""" Testing """

#test = TextBoxPage()
#test.collect_from_wrappers()
#test.insert_text_in_all(email='test@example.com', current_address='example address')
#test.get_results()
#for key in test.results:
#    print(f'{key} : {test.results[key]}')
#test.close_page()