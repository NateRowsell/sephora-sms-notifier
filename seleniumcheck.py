from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time

def check_for(url, xpath):

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        driver.quit()
        return True
    driver.quit()        
    return False
    
