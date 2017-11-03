#  IN THE NAME OF ALLAH

import urllib.request
from main import parser_agent
from bs4 import BeautifulSoup
import json
import ssl

parsed = []
text = []
all_data = json.load(open('input.json',encoding='utf-8'))

for data in all_data:

    g_context = ssl._create_unverified_context()
    parsed.append(BeautifulSoup(urllib.request.urlopen(data['link'], context=g_context).read(), "html.parser"))
    text.append(data['text'])

parser_agent(parsed, text)
