#  IN THE NAME OF ALLAH

import urllib.request
from main import parser_agent
from bs4 import BeautifulSoup
import json
import ssl

parsed = []
text = []
all_data = json.load(open('mashregh_mainimage.json',encoding='utf-8'))

for data in all_data:

    print(data['link'], "inja link \n\n", data["text"], "\n\n")

    g_context = ssl._create_unverified_context()
    parsed.append(BeautifulSoup(urllib.request.urlopen(data['link'], context=g_context).read(), "html.parser"))
    text.append(data['text'])

    # print(data['link'], "inja link \n\n", data["text"], "\n\n")
    # print(parsed[-1].prettify(), "\n $$$$ \n", text[-1], "\n^")

parser_agent(parsed, text)
