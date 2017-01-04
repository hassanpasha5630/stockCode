#link That will be web Scrapped
#https://finance.yahoo.com/quote/TMUS?p=TMUS
# This uses another logic to scrap data , data has been retrived perfectly
# parsing and checking to see if the stock price is worth selling
#issue : paring percentages 
#
import urllib
import urllib.request
import re
from bs4 import BeautifulSoup
#setiing up the parsing the link
theurl = "https://finance.yahoo.com/quote/TMUS?p=TMUS"
thepage = urllib.request.urlopen((theurl))
soup = BeautifulSoup(thepage,"html.parser")
#getting the title tag
print(soup.title.text)

value = soup.find('div',{"class":"D(ib) Fw(200) Mend(20px)"}).find('span').text
value_int = float(value)

#this is getting the prcenetage of the increase or Decrease
Drop_Increase = soup.find('div',{"class":"D(ib) Fw(200) Mend(20px)"}).find('span',{"class":"Fw(500) Pstart(10px) Fz(24px) C($dataGreen)"}).text

print(Drop_Increase)




print(value)

if value_int > 47 :
    print("Stock Greater than purchase Price")

else :
    print("Stock is going down")


#dealcaring list to store

Stock_Price_List = list()
Stock_Percentage_List = list()
Day_Date_List = list()


#inserting the percentage and the stock price to the list

Stock_Percentage_List.append(Drop_Increase)
Stock_Price_List.append(value_int)

#checking to see if the elemebt has been inserted into the list

# print(Stock_Price_List)
# print(Stock_Percentage_List)

#parsing the percentage

def tsplit(string, delimiters):
    """Behaves str.split but supports multiple delimiters."""

    delimiters = tuple(delimiters)
    stack = [string, ]

    for delimiter in delimiters:
        for i, substring in enumerate(stack):
            substack = substring.split(delimiter)
            stack.pop(i)
            for j, _substring in enumerate(substack):
                stack.insert(i + j, _substring)

    return stack

#print(re.split('( )+',Drop_Increase))

# code above was referenced http://code.activestate.com/recipes/577616-split-strings-w-multiple-separators/

a = Drop_Increase.split("( )")
print(a)

get_Per = list()
#
#get_Per.append(Stock_Percentage_List[0])
# percentage = get_Per[0]
#
# percentage_split = percentage.split("(").spl


# for spliter in a:
#     if(spliter is "("):
#         print("I am here")

# print(Drop_Increase)
#print(a)
#
print(get_Per)
#
# print(percentage_split)
