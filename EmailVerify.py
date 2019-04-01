from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_argument('headless')

browser = webdriver.Chrome(chrome_options=options)

def load_web():
    #launch url
    url = "https://login.live.com/"

    # create a new chrome session
    browser = webdriver.Chrome(chrome_options=options)
    browser.implicitly_wait(30)
    browser.get(url)


def login(email_address):

    login = browser.find_elements_by_xpath('//*[@id="i0116"]')
    login[0].send_keys(email_address)
    login[0].send_keys('\ue007')

    
def verify():

    try:
        browser.find_element_by_id("usernameError")
        return(False)
    except NoSuchElementException:
        return(True)

