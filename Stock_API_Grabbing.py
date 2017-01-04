#this is using another method to grab data
#http://altitudelabs.com/blog/web-scraping-with-python-and-beautiful-soup/

#import libraries
import urllib.request
import csv
from bs4 import BeautifulSoup
from datetime import datetime

#varbale for the URL

URL = " https://www.bloomberg.com/quote/TMUS:US "
#URL2
#URL#


#quesry the website and retun thehtml to the varable

page = urllib.request.urlopen(URL)
soup = BeautifulSoup(page,"html.parser")

#attar maps to see if the given attribute exisits
#this will remove the starting and trailing

name_box = soup.find('h1',attrs ={'class':'name'}).text.strip()

#this will remove the starting and trailing


###############################################################
#get the index price

price_box = soup.find('div', attrs={"class":'price'}).text.strip()



#this is me just error checking right now

print(name_box)
print(price_box)


##################### saving the price to an excel CSV

#open a scv file with append , so old data will not be erased

with open('index.csv','a') as csv_file:
    write = csv.writer(csv_file)
    write.writerow([name_box,price_box,datetime.now()])