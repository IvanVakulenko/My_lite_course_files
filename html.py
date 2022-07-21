import urllib
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')
count = 0
sums = 0
for tag in tags:

	x=int(tag.text)

	count = count.get(words,0) + 1

	sums = sums + x
print (count)
print (sums)