import re
from bs4 import BeautifulSoup
import urllib
import urllib.request
import csv
import time
from datetime import datetime


URL1 = "https://finance.yahoo.com/quote/tmus?ltr=1"
URL2 = "https://finance.yahoo.com/quote/TWTR?p=TWTR"
URL3 = "https://finance.yahoo.com/quote/aapl?ltr=1"
URL4 = "https://finance.yahoo.com/quote/AMDA?p=AMDA"

Links =[URL1,URL2,URL3,URL4]
Data = []
TypeCast = []

while True:
    now = datetime.now().strftime('%H%M')
    if '0830' <= now <= '0300' or '0830' <= now <= '1500' or '0200' <= now <= '0300' :
        for stocks in Links :


            page = urllib.request.urlopen(stocks)
            soup = BeautifulSoup(page,"html.parser")
            try:
                Stock_Name = soup.find("h1", attrs= {"class":"D(ib) Fz(18px)"}).text.strip()
import re
from bs4 import BeautifulSoup
import urllib
import urllib.request
import csv
import time
from datetime import datetime


URL1 = "https://finance.yahoo.com/quote/tmus?ltr=1"
URL2 = "https://finance.yahoo.com/quote/TWTR?p=TWTR"
URL3 = "https://finance.yahoo.com/quote/aapl?ltr=1"
URL4 = "https://finance.yahoo.com/quote/AMDA?p=AMDA"

Links =[URL1,URL2,URL3,URL4]
Data = []
TypeCast = []

while True:
    now = datetime.now().strftime('%H%M')
    if '0830' <= now <= '0300' or '0830' <= now <= '1500' or '0200' <= now <= '0400' :
        for stocks in Links :


            page = urllib.request.urlopen(stocks)
            soup = BeautifulSoup(page,"html.parser")
            try:
                Stock_Name = soup.find("h1", attrs= {"class":"D(ib) Fz(18px)"}).text.strip()
                print(Stock_Name)


            except:
                Stock_Name = soup.find('div', {"class": "D(ib)"}).find('h1').text.strip()
                print(Stock_Name)

          #      print("        ")
            try:
                Stock_Price = soup.find("span", attrs={"class":"Fw(b) Fz(36px) Mb(-4px)"}).text.strip()
                print(Stock_Price)
                typecasting = float(Stock_Price)
                TypeCast.append(typecasting)

           #     print("        ")
            except:
                Stock_Price = soup.find('div',{"class":"D(ib) Fw(200) Mend(20px)"}).find('span',{"class": " Fw(b) Fz(36px) Mb(-4px)"}).text
                print(Stock_Price)
                typecasting = float(Stock_Price)
                TypeCast.append(typecasting)

            #    print("        ")
            try :
                Percentage = soup.find("span", attrs={"class":"Fw(500) Pstart(10px) Fz(24px) C($dataRed)"}).text.strip()
                print(Percentage)
                print("Red")

             #   print("        ")
            except:
                Percentage =soup.find("span", attrs={"class":"Fw(500) Pstart(10px) Fz(24px) C($dataGreen)"}).text.strip()
                print(Percentage)
                print("Green")

            Data.append((Stock_Name, Stock_Price, Percentage))
            with open('MyStock4.csv', 'a') as csv_file:
                

                write = csv.writer(csv_file)
                for Stock_Name, Stock_Price, Percentage in Data:
                    # time2 = datetime.now()
                    print(Data)
                    write.writerow([Stock_Name, Stock_Price, Percentage, datetime.now().strftime("%H:%M:%S")])



              #  print("        ")


    else:
        print("Market is closed")
        break




   # typecating = int(Stock_Price)
   #TypeCast.append(typecating)
    print("          ")
    print("For Hassan")
    print("           ")
    print(TypeCast)
    print("        ")
    if(TypeCast[0] > 47):
        print("Tmobile Stock is up " , TypeCast[0])
        print("        ")
    else:
        print("Tmobile Stock is dropping" , TypeCast[0])
        print("        ")
    if(TypeCast[1] > 20) :
        print("Twitter Stock is up" ,TypeCast[1])
        print("        ")
    else:
        print("Twitter Stock is down",TypeCast[1])
        print("        ")
    if(TypeCast[2] > 120) :
        print("Apple Stock is up From purchase", TypeCast[2])
        print("        ")
    else:
        print("Apple Stock is going down ", TypeCast[2])
        print("        ")
    if(TypeCast[3] > 2):
        print("AMDA stock is up",TypeCast[3])
        print("        ")
    else :
        print("AMDA stock is going down",TypeCast[3])
        print("        ")

    print("sleeping for 5 sec")
    #time.sleep(30)
