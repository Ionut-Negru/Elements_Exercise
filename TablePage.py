from Driver import *
from TextBoxPage import TextBoxPage
import time

class TablePage(TextBoxPage):
    
    def __init__(self):
        super().__init__()
        self.set_wrappers_xpath("//div[@class='modal-body']/form[@id='userForm']/div[contains(@id,'wrapper')]")
        self.set_submit_button_xpath("//form[@id='userForm']/div/div/button[@id='submit']")
        
    def get_table_head(self):
        headers = self.browser.find_elements_by_xpath("//div[@class='web-tables-wrapper']/div/div/div/div[@class='rt-tr']/div")
        self.table_head = []
        for aux in headers:
            self.table_head.append(aux.text)
        return self.table_head
    
    def get_table_rows(self, row_length=0):
        rows = self.browser.find_elements_by_xpath("//div[@class='rt-table']/div[@class='rt-tbody']/div/div/div")
        table_data = []
        i = 0
        while i < len(rows):
            current_row = []
            for j in range(row_length):
                if i >= len(rows):
                    break
                else:
                    current_row.append(rows[i].text)
                    i = i + 1
            table_data.append(current_row)
        
        return table_data
    
    def get_actions_for_rows(self):
        actions = self.browser.find_elements_by_xpath("//div[@class='rt-table']/div[@class='rt-tbody']/div/div/div/div/span")
        for i in range(0, len(actions), 2):
            self.table[int(i/2)]['Action'] = [actions[i], actions[i+1]]
        
    def clear_empty_rows(self):
        aux = {}
        for x in self.table_head:
            aux[x] = ' '
            
        while aux in self.table:
            self.table.remove(aux)
            
    def get_table(self):
        head = self.get_table_head()
        data = self.get_table_rows(len(head))
        self.table = []
        for row in data:
            aux = {}
            for i in range(len(head)):
                aux[head[i]] = row[i]
            self.table.append(aux)
        self.clear_empty_rows()
        self.get_actions_for_rows()
    
    def add_new_row(*args):
        add_button = args[0].browser.find_element_by_xpath("//div[@class='web-tables-wrapper']/div/div/button[@id='addNewRecordButton']")
        add_button.click()
        args[0].collect_from_wrappers()
        args[0].insert_text_in_all(args[1:])
        args[0].submit_form()
        args[0].table.append(args[0].inputs)
        args[0].get_actions_for_rows()
    
    def delete_row(self, row=0):
        self.table[row]['Action'][1].click()
        del self.table[row]
    
    def update_row(*args):
        element = args[0].table[args[1]]['Action'][0]
        element.click()
        args[0].collect_from_wrappers()
        args[0].insert_text_in_all(args[2:])
        args[0].submit_form()
        args[0].get_table()
