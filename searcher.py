# IN THE NAME OF ALLAH

import urllib.request
from bs4 import BeautifulSoup

def search(parsed, address, text):
    s = ""
    print(address," inja address ", "inja text")
    # print(parsed.find_all('body')[0].select("div:nth-of-type(1)"))
    # print(parsed.select(address))
    arr = parsed.select(address)
    print(arr)
    for i in range(len(arr)):
        s += arr[i].get_text()

    return s.contains(text)