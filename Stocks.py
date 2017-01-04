#the code below is data scrapping but not getting the wanted to data


import requests
from bs4 import BeautifulSoup
#running this in the python shell as well

#requesting the data from the given website

r = requests.get("http://www.nasdaq.com/symbol/tmus/real-time" )

# this will show the content of the given page
r.content

#this will clean up the html code

soup = BeautifulSoup(r.content)
print(soup.prettify())

#soup in the varaible that we made this below will find all the a = links
soup.find_all("a")

# this for loop will find all the hyper links

for link in soup.find_all("a") :
    print (link)
    #get all the links
    link.get("herf")


#this should print out each text of the given list
    print(link.text)

    # this should give a link with text
    print(link.text) , link.get("herf")


#string subsitution

    "<a href='%s'>%s</a>"%(link.get("href"),link.text)



#finding general data using the class and div
g_data = soup.find_all("div",{"class":"genTable"})

#printing out data

for item in g_data:
    item.text

    #printout content the list
    item.contents


    print(item.contents[1].find_all("span",{"id","quotes_content_left_LastSale"}))
