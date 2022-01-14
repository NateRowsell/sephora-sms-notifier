from sys import exit
import time
from twilio.rest import Client 
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import bs4check

load_dotenv()
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
sendnumber = os.getenv("sendnumber")

# TODO this should be turned into collect_info.py function that can be used in main
url = input("Enter sephora product url: ")
pnumber = input("Enter your phone number: ")
checkurl = url.find("sephora")

#Verifying the url is correct
if checkurl == -1:
    print("Please enter a valid sephora url you entered: ", url, " Make sure the url contains sephora and skuid")
    exit()

 
#TODO for the in stock message splice a string from url for item title and add in the message string // can also pull this info when parsing data for instock much easier
instock = False
while instock == False:
    instock = bs4check.isinStock(url)
    time.sleep(5)

    if instock == False :

        print("Item is still out of stock") 
        continue

    elif instock == True :

        client = Client(account_sid, auth_token)
        urlmessage = "Your item is in stock " + url
        message = client.messages \
                        .create(
                            body=urlmessage,
                            from_=sendnumber,
                            to=pnumber
                        )
    else: 
        client = Client(account_sid, auth_token)
        urlmessage = "An error occured while monitoring your product please retry"
        message = client.messages \
                        .create(
                            body=urlmessage,
                            from_=sendnumber,
                            to=pnumber
                        )
        
print('Complete')
















