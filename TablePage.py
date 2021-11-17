from Driver import *
from TextBoxPage import TextBoxPage
import time

class TablePage(TextBoxPage):
    
    def __init__(self):
        super().__init__()
        self.set_wrappers_xpath("//div[@class='modal-body']/form[@id='userForm']/div[contains(@id,'wrapper')]")
        self.set_submit_button_xpath("//form[@id='userForm']/div/div/button[@id='submit']")
        
    def open_page(self):
        self.browser.get("http://demoqa.com/webtables")
        self.browser.maximize_window()
        
    def get_table(self, row_size=0):
        elements = self.browser.find_elements_by_xpath("//div[@class='rt-td' or @class='rt-resizable-header-content']")
        self.table_head = []
        for i in range(row_size):
            self.table_head.append(elements[i].text)
        
        self.table = []
        i = row_size
        while i in range(row_size,len(elements)):
            row = {}
            for j in range(row_size-1):
                row[self.table_head[j]] = elements[i].text
                i = i + 1
            try:
                actions = elements[i].find_elements_by_xpath(".//div/span")
                row[self.table_head[row_size-1]] = actions
            except Exception as e:
                print(e)
            finally:
                i = i + 1
            self.table.append(row)
        
        self.clear_empty_rows()
        
    def clear_empty_rows(self):
        aux = {'First Name': ' ', 'Last Name': ' ', 'Age': ' ', 'Email': ' ', 'Salary': ' ', 'Department': ' ', 'Action': []}
        while aux in self.table:
            self.table.remove(aux)
            
    def add_new_row(self, **kwargs):
        add_button = self.browser.find_element_by_xpath("//div[@class='web-tables-wrapper']/div/div/button[@id='addNewRecordButton']")
        add_button.click()
        self.collect_from_wrappers()
        self.insert_text_in_all(**kwargs)
    
    def delete_row(self, row=0):
        self.table[row]['Action'][1].click()
        del self.table[row]
    
    def update_row(self, row, **kwargs):
        element = self.table[row]['Action'][0]
        element.click()
        self.collect_from_wrappers()
        self.insert_text_in_all(**kwargs)


""" Testing """

#page = TablePage()
#page.get_table(7)
#page.update_row(2, email='example@test.com',salary='200')
#page.close_page()
