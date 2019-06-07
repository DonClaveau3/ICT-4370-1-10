"""
Author: Don Claveau
Create Date: 5/12/2019
Description: This script retrieves sample data from csv files 
Updates:

"""
import csv
from Holding import Holding
from datetime import date,timedelta,datetime
from Stock import Stock
from Bond import Bond
from Database import Database
from FormatHelper import DateFromMmddyyyyString


def GetHoldingsFor(investor,fileName,type="stock"):
    '''function to generate a set of sample holdings from a csv'''       
    holdings = []
    try:
        with open(fileName) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count =0
            for row in csv_reader:
                if line_count == 0:
                    pass
                else:
                    purchaseDate = DateFromMmddyyyyString(row[4])
                    if type=="bond":
                        stock = Bond(row[0],float(row[3]),float(row[5]),float(row[6]))
                    else:
                        stock = Stock(row[0],float(row[3]))
                    thisHolding=Holding.new(investor,stock,int(row[1]),float(row[2]),purchaseDate)
                    holdings.append(thisHolding)  
                    Database().Insert(thisHolding)                  
                line_count += 1
    except FileNotFoundError:
        print(f"File not found: {fileName}")    
    except ValueError:
        print(f"There was an issue getting values from {fileName} on line {line_count}")
    return holdings


