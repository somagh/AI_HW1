#  IN THE NAME OF ALLAH

import urllib.request
from main import parser_agent
from bs4 import BeautifulSoup
import json
import ssl

parsed = []
text = []

# all_data = json.load(open('irna_lead.json',encoding='utf-8'))

# for data in all_data:
#
#     g_context = ssl._create_unverified_context()
#     parsed.append(BeautifulSoup(urllib.request.urlopen(data['link'], context=g_context).read(), "html.parser"))
#     text.append(data['text'])

inp = input()

f = open(inp, 'r',encoding='utf-8')

num = 0

g_context = ssl._create_unverified_context()

while True:
    read = f.readline()
    if len(read) == 0:
        break
    if num % 2 == 1:
        text.append(read)
    else:
        parsed.append(BeautifulSoup(urllib.request.urlopen(read, context=g_context).read(), "html.parser"))
    num += 1

parser_agent(parsed, text)
