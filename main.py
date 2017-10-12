# in the name of god
import urllib.request
from bs4 import BeautifulSoup
parsed=BeautifulSoup(urllib.request.urlopen("http://ce.sharif.edu/~akowsary").read(),"lxml")
print(parsed.prettify())