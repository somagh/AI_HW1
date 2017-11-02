#  IN THE NAME OF ALLAH

import urllib.request
from main import parser_agent
from bs4 import BeautifulSoup

if __name__ == '__main__' :

    parsed = []
    text = []

    #doc = docx.Document("input.docx")

    f = open("input2.txt", 'r')


    n = int(f.read(1))
    f.readline()

    for i in range(n):

        while (True):
            link = f.readline()
            if link[0] != '\n' :
                print(link)
                parsed.append(BeautifulSoup(urllib.request.urlopen(link).read(),"html.parser"))
                break

        while (True):
            str = f.readline()
            if str[0] != '\n' :
                break

        while (True):
            str2 = f.readline()
            if len(str2) and str2[0] != '#' :
                str += str2
            else:
                break

        while (str[len(str)-1] == '\n') :
            str = str[:-1]

        text.append(str)

        print(i, " ", parsed[i].prettify(), "\n $$$$ \n", text[i], "\n^")



    parser_agent(parsed, text)



