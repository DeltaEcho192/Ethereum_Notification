#This is the inital setup file when starting the Program.
#Created By DeltaEcho192.


#This are all the modules that are Required
import bs4 as bs
import urllib.request
import re
import math

#These are the Var
counter = 0
url = 'https://ethereumprice.org/'
priceL = []
priceF = 0.0

#Gets the html file and cleans it up
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()

soup = bs.BeautifulSoup(html,'lxml')

#print(soup.find_all('meta'))

#Pulls out the specific line we would like.
for paragraph in soup.find_all('meta'):
    if counter == 4:
        priceString = paragraph
    counter = counter + 1

str1 = str(priceString)

#Pulls out the float values that we require.
priceFloat = re.findall("\d+\.\d+", str1)

#Converting some VAR
priceF = priceFloat[0]
priceF = float(priceF)
priceI = int(math.floor(priceF))
priceS = str(priceI)

#Writing the Price Value to A text file.
file = open('pricefloat.txt','w')
file.write(priceS)
file.close()
