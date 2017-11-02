# in the name of god

import urllib.request
from bs4 import BeautifulSoup

parsed = BeautifulSoup(urllib.request.urlopen("http://ce.sharif.edu/~akowsary").read(),"html.parser")
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


a = {}
if("salam" in a):
    print(a["salam"])
else:
    a["salam"] = 1
print(a["salam"])

def parser_agent(parsed, texts, address="body"):
    parsed_first = parsed[0].select(address)[0]
    parsed_first_children = list(parsed_first.children)
    n = len(parsed_first_children)
    # print(parsed_first_children, n)
    # for i in range(n):
    #     print(type(parsed_first_children[i]), "hi")
    parsed_per_name = {}

    for i in range(n):
        child_name = parsed_first_children[i].name
        if child_name is None:
            continue
        if child_name in parsed_per_name:
            parsed_per_name[child_name] += [parsed_first_children[i]]
        else:
            parsed_per_name[child_name] = [parsed_first_children[i]]
        print(i, parsed_first_children[i], child_name, parsed_per_name)

    max_point = 0
    max_address = ""
    for key in parsed_per_name:
        for i in range(len(parsed_per_name[key])):
            new_address = "{} > {}:nth-of-type({})".format(address, key, i)
            point = 0
            for text in texts:
                is_in_address = True # vez function (newAddress, function)
                if is_in_address:
                    point += 1
            if point > max_point:
                max_point = point
                max_address = new_address
    if max_point != texts:
        print("answer is {}".format(address))
    else:
        parser_agent(parsed, texts, max_address)

# parser_agent([parsed], ["salam"])