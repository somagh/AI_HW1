#  IN THE NAME OF ALLAH

import urllib.request
from main import parser_agent
from bs4 import BeautifulSoup
import json

parsed = []
text = []
all_data = json.load(open('input3.json',encoding='utf-8'))

for data in all_data:
    parsed.append(BeautifulSoup(urllib.request.urlopen(data['link']).read(),"html.parser"))
    text.append(data['text'])
    #print(parsed[-1].prettify(), "\n $$$$ \n", text[-1], "\n^")

parser_agent(parsed, text)
