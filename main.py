# in the name of god

import urllib.request
from bs4 import BeautifulSoup
from searcher import search

# parsed = BeautifulSoup(urllib.request.urlopen("http://ce.sharif.edu/~akowsary").read(),"html.parser")
# print (parsed.body.find_all('li')[0].a.get('href'))
# print (parsed.prettify())
# print(list(parsed.children))
# print([type(item) for item in list(parsed.children)] )
# x = parsed.body.find_all('a')[0].get_text()
# print (len(x), x)
# print (parsed.body.find_all('div')[0].name)
# parsed = parsed.find('body')
# print(parsed.prettify())
# print(parsed.select("body > nav > div"))
# print(parsed.select("ul > li"))
# felan = { "soup": [],"text": [] }


def parser_agent(parsed, texts, address="body"):
    parsed_first = parsed[0].select(address)[0]
    parsed_first_children = list(parsed_first.children)
    n = len(parsed_first_children)
    parsed_per_name = {}

    for i in range(n):
        child_name = parsed_first_children[i].name
        if child_name is None:
            continue
        if child_name in parsed_per_name:
            parsed_per_name[child_name] += [parsed_first_children[i]]
        else:
            parsed_per_name[child_name] = [parsed_first_children[i]]

    max_point = 0
    max_address = ""
    for key in parsed_per_name:
        for i in range(len(parsed_per_name[key])):
            if len(address) == 0:
                new_address = "{}:nth-of-type({})".format(key, i + 1)
            else:
                new_address = "{} > {}:nth-of-type({})".format(address, key, i + 1)
            point = 0
            for j in range(len(texts)):
                is_in_address = search(parsed[j], new_address, texts[j])
                if is_in_address:
                    point += 1
            print("inja link", new_address, point, max_point)
            if point > max_point:
                max_point = point
                max_address = new_address
    if max_point != len(texts):
        print("answer is {}".format(address))
    else:
        parser_agent(parsed, texts, max_address)
