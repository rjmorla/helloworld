from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import numpy as np
import cv2

mysite = "https://en.wikipedia.org/wiki/Pepe_the_Frog"

headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169'}

link = Request(mysite, headers = headers)
link_url = urlopen(link)

soup = BeautifulSoup(link_url.read(), 'lxml')

img = soup.find("div", {'id': 'mw-content-text'}).find("img")["src"]

r = urlopen("https:"+img)
image = np.asarray(bytearray(r.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)
image = cv2.applyColorMap(image, cv2.COLORMAP_HOT)
cv2.imshow("feelsgoodman", image)
cv2.waitKey()
