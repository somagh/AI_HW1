# in the name of god
import urllib.request
from bs4 import BeautifulSoup
parsed=BeautifulSoup(urllib.request.urlopen("http://ce.sharif.edu/~akowsary").read(),"html.parser")
#print (parsed.body.find_all('li')[0].a.get('href'))
#print (parsed.prettify())
#print(list(parsed.children))
# print([type(item) for item in list(parsed.children)] )
x = parsed.body.find_all('a')[0].get_text()
print (len(x), x)
#print (parsed.body.find_all('div'))
