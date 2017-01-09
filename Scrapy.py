import re
from bs4 import BeautifulSoup
import urllib
import urllib.request
import csv
import time
import sqlite3
#import datetime
from datetime import datetime
from collections import OrderedDict


URL1 = "https://finance.yahoo.com/quote/tmus?ltr=1"
URL2 = "https://finance.yahoo.com/quote/TWTR?p=TWTR"
URL3 = "https://finance.yahoo.com/quote/aapl?ltr=1"
URL4 = "https://finance.yahoo.com/quote/AMDA?p=AMDA"

Links =[URL1,URL2,URL3,URL4]
Data = []
TypeCast = []
#---------Creating Database-----------------------------------------------------------------------------------#
database = sqlite3.connect('stocks12.db')
cursor = database.cursor()
try:
    cursor.execute('''CREATE TABLE Stocks( Stock_Name TEXT , Stock_Price REAL, Stock_Percentage TEXT ,Time REAL, Date REAL ,Day TEXT  )''')
    database.commit()
except:
    print("Already created table")



#----------------------------------------------------------------------------------------------------------------#
while True:
    now = datetime.now().strftime('%H%M')
    day_of_the_week = datetime.today().date().weekday()
    if day_of_the_week is not 1 or 5: # checking to see if the the day is between - monday -> Friday
        #fix the time later
        if '0830' <= now <= '0300' or '0830' <= now <= '1500' or '0000' <= now <= '1900' :
            for stocks in Links :


                page = urllib.request.urlopen(stocks)
                soup = BeautifulSoup(page,"html.parser")
                try:
                    Stock_Name = soup.find("h1", attrs= {"class":"D(ib) Fz(18px)"}).text.strip()
                    print(Stock_Name)


                except:
                    try:
                    #print("ERROR Grabing stock name")
                        Stock_Name = soup.find('div', {"class": "D(ib)"}).find('h1').text.strip()
                        print(Stock_Name)
                    except:
                        print("ERROR stock name")
                        break;

              #      print("        ")
                try:
                    Stock_Price = soup.find("span", attrs={"class":"Fw(b) Fz(36px) Mb(-4px)"}).text.strip()
                    print(Stock_Price)
                    try:
                        typecasting = float(Stock_Price)
                        TypeCast.append(typecasting)
                    except:
                        print("CAN NOT TYPE CAST")
               #     print("        ")
                except:
                    Stock_Price = soup.find('div',{"class":"D(ib) Fw(200) Mend(20px)"}).find('span',{"class": " Fw(b) Fz(36px) Mb(-4px)"}).text
                    print(Stock_Price)
                    #typecasting = float(Stock_Price)
                    TypeCast.append(typecasting)

                #    print("        ")
                try :
                    Percentage = soup.find("span", attrs={"class":"Fw(500) Pstart(10px) Fz(24px) C($dataRed)"}).text.strip()
                    print(Percentage)
                    print("Red")
                    #typecasting_percentages =  float(Percentage)
                    Data.append((Stock_Name, Stock_Price, Percentage))


                 #   print("        ")
                except:
                    Percentage =soup.find("span", attrs={"class":"Fw(500) Pstart(10px) Fz(24px) C($dataGreen)"}).text.strip()
                    print(Percentage)
                    print("Green")
                    #typecasting_percentages = float(Percentage)
                    Data.append((Stock_Name, Stock_Price, Percentage))

                cursor.execute('''INSERT INTO Stocks(Stock_Name,Stock_Price,Stock_Percentage,Time,Date,Day)VALUES(?,?,?,?,?,?)''',
                               (Stock_Name,typecasting,Percentage,datetime.now().strftime("%H:%M:%S"),time.strftime("%x"),
                                datetime.now().strftime("%A")))
                database.commit()

                with open('MyStock10.csv', 'a') as csv_file:





                    write = csv.writer(csv_file)
                    for Stock_Name, Stock_Price, Percentage in Data:
                        # time2 = datetime.now()
                        list(OrderedDict.fromkeys(Data))

                        write.writerow([Stock_Name, Stock_Price, Percentage, datetime.now().strftime("%H:%M:%S")])


                        #  print("        ")


        else:
            print("Market is closed")
            break

        # cursor.execute("SELECT * FROM Stocks")
        # print(cursor.fetchall())


    else:
        print("The Market is closed on Weekends")
        break

try:
    cursor.execute('''CREATE TABLE TMOBILE AS Select * From Stocks where Stock_Name Like "T-Mobile US, Inc.(TMUS)" ''')
    database.commit()
except:
    print("IAM HERE ")






    # typecating = int(Stock_Price)
   # #TypeCast.append(typecating)
   #  print("          ")
   #  print("For Hassan")
   #  print("           ")
   #  print(TypeCast)
   #  print("        ")
   #  if(TypeCast[0] > 47):
   #      print("Tmobile Stock is up " , TypeCast[0])
   #      print("        ")
   #  else:
   #      print("Tmobile Stock is dropping" , TypeCast[0])
   #      print("        ")
   #  if(TypeCast[1] > 20) :
   #      print("Twitter Stock is up" ,TypeCast[1])
   #      print("        ")
   #  else:
   #      print("Twitter Stock is down",TypeCast[1])
   #      print("        ")
   #  if(TypeCast[2] > 120) :
   #      print("Apple Stock is up From purchase", TypeCast[2])
   #      print("        ")
   #  else:
   #      print("Apple Stock is going down ", TypeCast[2])
   #      print("        ")
   #  if(TypeCast[3] > 2):
   #      print("AMDA stock is up",TypeCast[3])
   #      print("        ")
   #  else :
   #      print("AMDA stock is going down",TypeCast[3])
   #      print("        ")

print("sleeping for 5 sec")
  #  time.sleep(2)

    
