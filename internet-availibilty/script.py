from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# This is the URL for the internet availibilty checker site. Move to more logical place later.
internet_checker_URL = 'https://www.t-mobile.com/isp/eligibility'

# This is will be the references to all of the webdrivers. There will probably need to be logic that determines which webdriver/browser is available and which one will be used to execute the given tasks but for now we're just gonna have one instance and assume we know that the user has chrome installed and the correct version.
path_to_chromedriver = './chromedriver'

# Instance of our webdriver.
driver = webdriver.Chrome(path_to_chromedriver)

# Open instance of driver @T-Mobile internet availibilty checker url.
driver.get(internet_checker_URL)

# Return current URL as string. This will be useful when/if we need to monitor for a change in the URL.
def current_str_url_is() -> str:
    return driver.current_url

# Check if given element exists. Return boolean. This will be useful when grabing elements. This will prevent grabbing elements that dont exist and crashing the scripts. Maybe run a check for all needed elements to preform a task before it is executed?
def element_does_exist(element_class) -> bool:
    try:
        driver.find_element_by_class_name(element_class)
    except NoSuchElementException:
        return False
    return True


