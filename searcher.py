# IN THE NAME OF ALLAH

import urllib.request
from bs4 import BeautifulSoup

def search(address, text):
    s = address.get_text()
    return s.contains(text)