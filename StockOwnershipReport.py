"""
Author: Don Claveau
Create Date: 4/24/2019
Description: This module contains functions for printing a report of holdings for a user. 
Updates:
        5/3/2019 Add a section for bonds
        5/12/2019 Allow output to file
"""
from Holding import Holding
from Stock import Stock
from Bond import Bond
from Investor import Investor
from FormatHelper import as_currency,as_percent

class StockOwnershipReport():
    _lastId=0

    def __init__(self, investor, holdings):
        self.id = self._nextId()
        self.investor = investor
        self.holdings = holdings
        self.report = ''
        self.MakeReport()

    def MakeReport(self):
        '''creates report as string'''
        headerText = "Holdings owned by "+self.investor.name.upper()
        self.append_reportHeader(headerText)
        holdingsForName = [holding for holding in self.holdings if holding.investor.name==self.investor.name]
        stocks = [holding for holding in holdingsForName if isinstance(holding.stock,Bond)==False]
        bonds = [holding for holding in holdingsForName if isinstance(holding.stock,Bond)]
        self.append_stockOwnershipTableHeader()
        self.append_stockOwnershipTableBody(stocks)
        self.append_dashLine()
        self.append_bondOwnershipTableHeader()
        self.append_stockOwnershipTableBody(bonds)     
        self.append_reportFooter()

    def _nextId(self):
        '''gets the next available id'''
        StockOwnershipReport._lastId=StockOwnershipReport._lastId+1
        return StockOwnershipReport._lastId

    def printToFile(self,outputFileName):
        '''prints report to file'''
        try:
            with open(outputFileName,'w') as file:
                file.write(self.report)
        except:
            print("Unable to print report to file.")
            
    def printToConsole(self):
        '''prints report of holdings for an investor'''
        print(self.report)
   
    def appendAsLine(self,string=''):
        '''appends string to report as a line'''
        self.report=self.report+string+'\n'

    def append_dashLine(self,length=65):
        '''append a line of dashes; params: int length (default 65)'''
        self.appendAsLine("-"*length)

    def append_centered(self,text,lineLength=65):
        '''function to append a string centered within a certain line length'''
        textLength = len(text)
        if (textLength>lineLength):
                self.appendAsLine(text)
        else:
                bufferLength = int((lineLength-textLength)/2)
                bufferString = " "*bufferLength
                self.appendAsLine('{}{}{}'.format(bufferString,text,bufferString))

    def append_reportHeader(self,text):
        '''function to append a formatted report header'''
        self.appendAsLine('')
        self.append_dashLine()
        self.append_centered(text)
        self.append_dashLine()    

    def append_stockOwnershipTableHeader(self):
        '''function to append a formatted table header'''
        self.append_stockOwnershipRow("STOCK","SHARE#","EARNINGS/LOSS","YEARLY EARNING/LOSS")
        self.append_dashLine()

    def append_bondOwnershipTableHeader(self):
        '''function to append a formatted table header'''
        self.append_stockOwnershipRow("BOND","QUANTITY#","EARNINGS/LOSS","YEARLY EARNING/LOSS")
        self.append_dashLine()

    def append_stockOwnershipTableBody(self,holdings):
        '''function to append a formatted table body'''
        for holding in holdings:
                gainLossAmount = holding.calculateGainLossAmount() 
                yearlyRate = holding.calculateYearlyEarningLossRate()
                self.append_stockOwnershipRow(holding.stock.symbol.upper(),str(holding.quantity),as_currency(gainLossAmount),as_percent(yearlyRate))

    def append_stockOwnershipRow(self,symbol,quantity,gainLoss,yearlyRate):
        '''function to append a row of values with fixed column widths'''
        self.appendAsLine('{:10s}{:15s}{:20s}{:20}'.format(symbol,quantity,gainLoss,yearlyRate))

    def append_reportFooter(self):
        '''function to append a formatted footer'''
        self.append_dashLine()
        self.appendAsLine('')

