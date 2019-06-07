"""
Author: Don Claveau
Create Date: 4/6/2019
Description: This script prompts the user for their name, retrieves holdings associated with that name, calculates gains/losses,
    and reports the information back to the console. 
Updates:
    4/13/2019 Add lists
    4/18/2019 Refactor using dictionaries
    4/24/2019 Refactor functions into modules
    5/3/2019 Refactor modules into classes
    5/12/2019 Allow input and output from file
    5/26/2019 Add a graph generator for stock history
"""

from Investor import Investor
import SampleData
from StockOwnershipReport import StockOwnershipReport
from Database import Database
import StockHistoryGraph

def main(stockHoldingsFileName,bondHoldingsFileName,stockHistoryJSONFilePath,outputDirectory):
    '''script entry point'''
    #create report from csv files
    #ReportFromFiles(stockHoldingsFileName,bondHoldingsFileName,outputDirectory)

    #create line graph from json
    lineGraphOutputFilePath = outputDirectory + '/lineGraph.png'
    StockHistoryGraph.MakeLineGraph(stockHistoryJSONFilePath,lineGraphOutputFilePath)

def ReportFromFiles(stockHoldingsFileName,bondHoldingsFileName,outputDirectory):
    '''Handles the ownership report experience'''
    db = Database()
    db.Initialize()

    #Elicit name from the user
    name = str(input("Hey, what's your name? "))
    investor = Investor.new(name)
    db.Insert(investor)

    #Load holdings from file to database    
    SampleData.GetHoldingsFor(investor,stockHoldingsFileName)
    SampleData.GetHoldingsFor(investor,bondHoldingsFileName,"bond")
    #Load holdings from database
    holdings = db.GetHoldings()

    #print report
    report = StockOwnershipReport(investor,holdings)  
    outputFileName = outputDirectory + '/output.txt'  
    report.printToFile(outputFileName)
    report.printToConsole()

directory = 'C:/Users/doncl/OneDrive/Documents/DU Coursework/ICT4370 - Python/Unit8-Visualization/Claveau.Don.Unit8'
stockHoldingsFileName = directory + '/Lesson6_Data_Stocks.csv'
bondHoldingsFileName = directory + '/Lesson6_Data_Bonds.csv'
stockHistoryJSONFilePath = directory + '/AllStocks.json'
outputFileName = directory + '/output.txt'

main(stockHoldingsFileName,bondHoldingsFileName,stockHistoryJSONFilePath,directory)