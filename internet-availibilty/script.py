from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

path_to_chromedriver = './chromedriver'
internet_checker_URL = 'https://www.t-mobile.com/isp/eligibility'

'''
    1.open an instance of the driver.
    2.open driver @'https://www.t-mobile.com/isp/eligibility'
    3.find elements needed to enter lead information.

        - phone number input: formated string as phone number.
            element identifier: class=''

        - address input: formatted string as address.
            element identifier: class=''

'''
driver = webdriver.Chrome(path_to_chromedriver)
driver.get(internet_checker_URL)








'''returns an instance of the current url of the driver.'''
def current_str_url_is() -> str:
    return driver.current_url

''' check if there is an element with the name of this class'''
def element_does_exist_with(element_class) -> bool:
    try:
        driver.find_element_by_class_name(element_class)
    except NoSuchElementException:
        print('could not find any elements with an class identifier of ${element_class}')
        return False
    return True
'''return the first element with the class name'''
def grab_element_with_class(element_class):
    pass



