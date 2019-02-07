import requests
from bs4 import BeautifulSoup
from os.path import basename
import os
r = requests.get("http://www.etudehouse.com/kr/produck.do?method=view&prdCd=102001343&sapCd=")
soup=BeautifulSoup(r.content,"lxml")
links=soup.findAll("img",{"onerror":True,"alt":True,"src":True})]

for links in links:
if "http" in link.get('src'):
image_links=link.get('src'):
if image_links.endswith('.jpg'):
with open(basename(image_links),"wb") as f:
f.write(requests.get(image_links).content)