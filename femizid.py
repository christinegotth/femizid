import requests 
from bs4 import BeautifulSoup
import re 
import json
import pandas as pd

#var maplistScriptParamsKo
  
data = "http://www.onebillionrising.de/femizid-opfer-meldungen-2019/"
r = requests.get(data) 
  
soup = BeautifulSoup(r.content, 'html.parser') 

pattern = re.compile(r"var maplistScriptParamsKo\s+=\s+(\{.*?\});\n")
script = soup.find("script", text=pattern)

data = pattern.search(script.text).group(1)

data = json.loads(data)

print(data)
