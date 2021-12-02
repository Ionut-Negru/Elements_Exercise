from Driver import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class FormPage(Driver):
    
    def __init__(self):
        super().__init__()
        self.open_page("https://demoqa.com/automation-practice-form")
        self.get_elements()
        self.form_dict={
            'male': 'gender-radio-1',
            'female': 'gender-radio-2',
            'other': 'gender-radio-3',
            'sports': 'hobbies-checkbox-1',
            'reading': 'hobbies-checkbox-2',
            'music': 'hobbies-checkbox-3',
            'state': 'react-select-3-input',
            'city': 'react-select-4-input'
            }
        
        
    def get_elements(self):
        wrappers = self.browser.find_elements_by_xpath("//form[@id='userForm']/div[@class='mt-2 row']")
        self.elements = {}
        for element in wrappers:
            try:
                inputs = element.find_elements_by_xpath(".//*[self::input or self::textarea]")

                for input in inputs:
                    self.elements[input.get_attribute('id')] = input
            except Exception as e:
                print(e)
    
    def set_name(self, first_name='', last_name=''):
        self.elements['firstName'].clear()
        self.elements['lastName'].clear()
        self.elements['firstName'].send_keys(first_name)
        self.elements['lastName'].send_keys(last_name)
    
    def select_gender(self, gender=''):
        match gender:
            case 'male':
                ActionChains(self.browser).move_to_element(self.elements[self.form_dict["male"]]).click(self.elements[self.form_dict["male"]]).perform()
            case 'female':
                ActionChains(self.browser).move_to_element(self.elements[self.form_dict["female"]]).click(self.elements[self.form_dict["female"]]).perform()
            case 'other':
                ActionChains(self.browser).move_to_element(self.elements[self.form_dict["other"]]).click(self.elements[self.form_dict["other"]]).perform()
            case _:
                return 'The selected gender is not an option'
            
    def set_email(self, email=''):
        self.elements['userEmail'].clear()
        self.elements['userEmail'].send_keys(email)

    def set_user_number(self, number=''):
        self.elements['userNumber'].clear()
        self.elements['userNumber'].send_keys(number)
    
    def select_day_of_birth(self, day=1):

        """ Select Day """
        day_elements = self.browser.find_elements_by_xpath("//div[@class='react-datepicker__week']/div")
        previous_month_days = 0
        for days in day_elements:
            if days.text == '1':
                break
            else:
                previous_month_days += 1
                
        print(previous_month_days)
        day = previous_month_days + day - 1
        day_elements[day].click()
    
    def select_month_of_birth(self, month=1):
        """ Select Month """
        month_element = self.browser.find_element_by_xpath("//select[@class='react-datepicker__month-select']")
        month_element.click()
        month_options = month_element.find_elements_by_xpath(".//option")
        month_options[month-1].click()
        self.browser.find_element_by_xpath("//div[@class='react-datepicker__header']/div[1]").click()
        
    def select_year_of_birth(self, year=2000):
        """ Select Year """
        year_element = self.browser.find_element_by_xpath("//select[@class='react-datepicker__year-select']")
        year_element.click()
        for option_year in year_element.find_elements_by_xpath(".//option"):
            if option_year.text == str(year):
                option_year.click()
                break
        self.browser.find_element_by_xpath("//div[@class='react-datepicker__header']/div[1]").click()
        
    def set_user_date_of_birth(self, year=2000, month=1, day=1):
        if year < 0:
            print("Unvalid year")
        elif month < 1:
            print("Unvalid month")
        elif day < 1:
            print("Unvalid day")
        
        self.elements['dateOfBirthInput'].send_keys('x')
        self.select_month_of_birth(month)
        self.select_year_of_birth(year)
        self.select_day_of_birth(day)
    
    def set_subjects(self, subjects=''):
        self.elements['subjectsInput'].clear()
        self.elements['subjectsInput'].send_keys(subjects)
        self.elements['subjectsInput'].send_keys(Keys.ENTER)
    
    def select_hobbie(self, hobbie=''):
        element = self.elements[self.form_dict[hobbie]]
        ActionChains(args[0].browser).move_to_element(element).perform()
        try:
            element.click()
        except:
            ActionChains(args[0].browser).move_to_element(element).send_keys(Keys.PAGE_DOWN).move_to_element(element).click(element).perform()
            
    
    def set_current_address(self, address=''):
        self.elements['currentAddress'].clear()
        self.elements['currentAddress'].send_keys(address)
    
    def upload_photo(self, photo_path=''):
        element = self.elements['uploadPicture']
        element.send_keys(photo_path)
    
    def select_state_option(self, option=1):
        state_element = self.elements[self.form_dict['state']]
        state_element.send_keys('')
        ActionChains(self.browser).click(state_element).perform()
        options = self.browser.find_elements_by_xpath("//div[contains(@id, 'select-3-option')]")
        options[option].click()
        
    def select_city_option(self, option=1):
        city_element = self.elements[self.form_dict['city']]
        city_element.send_keys('')
        ActionChains(self.browser).click(city_element).perform()
        options = self.browser.find_elements_by_xpath("//div[contains(@id, 'select-4-option')]")
        options[option].click()
        
    def select_state_and_city(self, state_option='', city_option=''):
        self.select_state_option(state_option)
        self.select_city_option(city_option)
    
    def get_results(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            elements = args[0].browser.find_elements_by_xpath("//table[@class='table table-dark table-striped table-bordered table-hover']/tbody/tr/td")
            args[0].results = {}
            for i in range(0, len(elements), 2):
                args[0].results[elements[i].text] = elements[i+1].text
        return wrapper
    
    @get_results
    def submit_form(self):
        element = self.browser.find_element_by_xpath("//button[@id='submit']")
        try:
            element.click()
        except:
            ActionChains(self.browser).send_keys(Keys.PAGE_DOWN).move_to_element(element).click(element).perform()
    
    
                
""" Testing """
#page = FormPage()
#page.set_name('Ionut', 'Negru')
#page.set_email('test@example.com')
#page.select_gender('male')
#page.set_user_number('0757582322')
#page.set_user_date_of_birth(1999, 5, 7)
#page.set_subjects('Math')
#page.select_hobbie('sports')
#page.set_current_address('A fictive address')
#page.upload_photo('C:\\Users\\INegru\\Desktop\\nature.jfif')
#page.select_state_and_city(0, 1)
#page.submit_form()
#page.close_page()