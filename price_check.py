#This file runs every so often then checks weather or not the change is big
#enough and then sends a notifications to make sure the User knows when the
#price has changed.
#Created By DeltaEcho192.


#This are all the modules that are Required
import bs4 as bs
import urllib.request
import re
import math
from plyer import notification as n

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

#Open File to check for the stored Value.
file = open('pricefloat.txt','r')
oldpriceS = file.read()
file.close()

#Compares the Old price to the new price and calculates the change in price.
oldpriceI = int(oldpriceS)
deltapriceI = priceI - oldpriceI

#If the change is big enough it sends a notification.
if deltapriceI > 5:
    deltapriceS = str(deltapriceI)
    stdmessageupS = "The price has changed by +"
    stdmessageup1S = stdmessageupS + deltapriceS
    n.notify(title='Etherium Price', message=stdmessageup1S)
elif deltapriceI < -5:
    deltaprice1S = str(deltapriceI)
    stdmessagedownS = "The price has changed by "
    stdmessagedown1S = stdmessagedownS + deltaprice1S
    n.notify(title='Etherium Price', message=stdmessagedown1S)
