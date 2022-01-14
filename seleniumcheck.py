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
    
#These import are only needed for selenium 
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# import ssl
# from seleniumcheck import check_for
# These variables are only needed for selenium in main.py 
# Ignore SSL certificate errors for https 
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# xpath = ("//button[@data-at='out_of_stock_btn']")