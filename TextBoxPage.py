
from Driver import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class TextBoxPage(Driver):
    
    def __init__(self):
        super().__init__()
        self.submit_xpath = "//form[@id='userForm']/div/div/button[@id='submit']"
        self.inputs = {}
        self.wrappers_xpath = "//div[@class='text-field-container']/form[@id='userForm']/div[contains(@id,'wrapper')]"
        
    def collect_from_wrappers(self):
        element = self.browser.find_elements_by_xpath(self.wrappers_xpath)
        self.labels = {}
        i = 0
        for aux in element:
            label = 'placeholder'+str(i)
            we = ''
            try:
                we = aux.find_element_by_xpath(".//*[self::input or self::textarea]")
                label = aux.find_element_by_xpath(".//label").text
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
        target.clear()
        target.send_keys(text)
        
    
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
        i = 0
        for aux in args[0].labels:
            args[0].insert_text(args[0].labels[aux],args[1][i])
            args[0].inputs[aux] = args[1][i]
            i = i + 1
        
    def get_result_by_name(self, name=''):
        return self.results[name]
