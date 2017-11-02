# IN THE NAME OF ALLAH

import urllib.request
from bs4 import BeautifulSoup

def search(parsed, address, text):
    s = ""
    arr = parsed.select(address)

    for i in range(len(arr)):
        s += arr[i].get_text()

    return s.contains(text)