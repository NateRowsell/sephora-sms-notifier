from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import ssl
from sys import exit
import time
from seleniumcheck import check_for
from twilio.rest import Client 
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests


load_dotenv()

account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
sendnumber = os.getenv("sendnumber")

# Ignore SSL certificate errors for https // might not need this with bs4 only selenium
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# TODO this should be turned into collect_info.py function that can be used in main
url = input("Enter sephora product url: ")
pnumber = input("Enter your phone number: ")
checkurl = url.find("sephora")
xpath = ("//button[@data-at='out_of_stock_btn']")

#Verifying the url is correct
if checkurl == -1:
    print("Please enter a valid sephora url you entered: ", url, " Make sure the url contains sephora")
    exit()

instock = False 

while instock == False:
    instock = check_for(url, xpath)
    time.sleep(5)
    if instock == False :
        print("Item is still out of stock") 
        continue
    else: 
        break

#TODO for the message splice a string from url for item title and add in the message string
client = Client(account_sid, auth_token)
urlmessage = "Your item is in stock " + url

if instock == True:
    message = client.messages \
                    .create(
                        body=urlmessage,
                        from_=sendnumber,
                        to=pnumber
                    )

print('Complete')
















