from multiprocessing.spawn import is_forking
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

path_to_chromedriver = './chromedriver'
internet_checker_URL = 'https://www.t-mobile.com/isp/eligibility'

'''dictionary of types needed for proceess that follow the naming conveniton name: element identifier'''
elements_needed = {
    'phone_input_id': 'mat-input-0',
    'address_input': 'mat-input-1'
}

'''launch driver at specific site URL'''
def launch_browser_at(url):
        driver.get(url)

'''check if all elements needed for automation exist return'''
def all_elements_needed_exist(elements) -> bool:
    for element, id in elements_needed.values():
        if element_does_exist_with(id):
            continue
        else:
            print('cant find elements needed to run.')
            return False
    return True


'''returns an instance of the current url of the driver.'''
def current_str_url_is() -> str:
    return driver.current_url

''' checks if an element with the ID exists'''
def element_does_exist_with(element_id) -> bool:
    try:
        driver.find_element_by_id(element_id)
    except NoSuchElementException:
        print('could not find any element with the ID ${element_id}')
        return False
    return True

'''return the first element with ID and returns it'''
def grab_element_with_id(element_id):
     if element_does_exist_with(element_id):
         elm = driver.find_element_by_id(element_id)
         return elm


'''
    1.open an instance of the driver.
    2.open driver @'https://www.t-mobile.com/isp/eligibility'
    3.find elements needed to enter lead information.

        - phone number input: formated string as phone number.

            element:
            -------
            <input autocomplete="tel" class="mat-input-element mat-form-field-autofill-control cdk-text-field-autofill-monitored ng-untouched ng-pristine ng-invalid" mask="(000) 000-0000" matinput="" name="phone" type="tel" id="mat-input-0" aria-invalid="false" aria-required="false">
            -------
        - address input: formatted string as address.

            element:
            -------
            <input autocorrect="off" class="mat-autocomplete-trigger mat-input-element mat-form-field-autofill-control cdk-text-field-autofill-monitored ng-untouched ng-pristine ng-invalid" matinput="" name="address" type="text" autocomplete="off" role="combobox" aria-autocomplete="list" aria-expanded="false" aria-haspopup="true" id="mat-input-1" aria-invalid="false" aria-required="false">
            -------
'''

'''create instance of driver.'''
driver = webdriver.Chrome(path_to_chromedriver)
launch_browser_at(internet_checker_URL)

# use the all_elements_exist() here once it works.
if element_does_exist_with('mat-input-0'):
    print('found first elm')
else:
    print('1 no good')

if element_does_exist_with('mat-input-1'):
    print('found second elm')
else:
    print('2 no good.')




