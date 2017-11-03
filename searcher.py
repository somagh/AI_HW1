# IN THE NAME OF ALLAH

import urllib.request
from bs4 import BeautifulSoup


def search(parsed, address, text):
    print(address," inja address ", "inja text")

    s = ""
    arr = parsed.select(address)

    for i in range(len(arr)):
        s += arr[i].get_text()

    ss = ""
    for i in range(len(s)):
        if(s[i] != '\n' and s[i] != ' ' and s[i] != '\t' and ord(s[i]) != 13):
            print("\n", i, " jk ", ss, " \n", s[i], "kfc", ord(s[i]), "\n\n")
            ss += s[i]

    s = ss;
    #print("\nFOR !!!!!!!!\n")

    texts = ""
    for i in range(len(text)):
        if(text[i] != '\n' and text[i] != ' ' and text[i] != '\t'):
            texts += text[i]

    text = texts;

    # s = s.replace(" ", "")
    # s = s.replace("\n", " ")
    # text = text.replace(" ", "")
    # text = text.replace("\n", "")

    print(arr, s.find(text) >= 0, text, "inja search", s, len(s), " \n\n\n\n\n\n\n\n\n\n\ninja arvandi \n\n\n")

    return s.find(text) >= 0