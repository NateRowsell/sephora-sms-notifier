from bs4 import BeautifulSoup
import requests

# right now when copying url you need to click on exact item size or color for this to work // need to test more cases on different item types
oosurl = "https://www.sephora.com/ca/en/product/charlotte-tilbury-mini-pillow-talk-lip-duo-P458268?icid2=value%20sets:p458268:product&skuId=2339620"
instockurl = "https://www.sephora.com/ca/en/product/charlotte-tilbury-mini-pillow-talk-lip-duo-P458268?icid2=value%20sets:p458268:product&skuId=2447738"

url = instockurl
sku = url.split("skuId=")[1]
sku = sku.split("&")[0]



headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
page = requests.get(url, headers=headers)
print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')
data = soup.prettify()
content = data.split('"')


def isinStock(content):

    """""
    content[count+1] stock
    content[count+5] sku

    """
    instock = "http://schema.org/InStock"
    count = 0

    for i in content:
        count += 1
        if i == "availability":
            print(content[count+5])
            print(content[count+1])
            if content[count+5] == sku and content[count+1] == instock:
                return True


print(isinStock(content))


