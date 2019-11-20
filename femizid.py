import requests 
from bs4 import BeautifulSoup
import re 
import pandas as pd
  
URL = "http://www.onebillionrising.de/femizid-opfer-meldungen-2019/"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') 

cases = re.search("(Reine Quellensammlung ohne Garantie auf Richtigkeit oder Vollständigkeit)", soup)

print(cases.prettify())