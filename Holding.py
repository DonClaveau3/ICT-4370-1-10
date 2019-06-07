"""
Author: Don Claveau
Create Date: 4/24/2019
Description: This module contains functions for creating and processing stock holdings. 
Updates:
    5/3/2019 Refactor to a class
"""

from datetime import date,timedelta

class Holding():
    _lastId = 0
    
    def __init__(self, id, investor,stock,quantity,purchasePrice,purchaseDate):
        self.investor = investor
        self.stock = stock
        self.purchaseId = id
        self.quantity = quantity
        self.purchasePrice = purchasePrice
        self.purchaseDate = purchaseDate
    
    @classmethod
    def new(self,investor,stock,quantity,purchasePrice,purchaseDate):
        thisHolding = Holding(self._nextId(),investor,stock,quantity,purchasePrice,purchaseDate)        
        return thisHolding
    
    @classmethod
    def _nextId(cls):
        '''gets the next available id'''
        Holding._lastId=Holding._lastId+1
        return Holding._lastId

    def calculateGainLossAmount(self):
        '''returns total amount of gain/loss'''
        priceDifference = self.stock.currentValue-self.purchasePrice
        gainLossAmount = round(self.quantity*priceDifference,2)
        return gainLossAmount

    def calculateYearlyEarningLossRate(self):
        '''returns average annual earning rate'''
        percentChange = ((self.stock.currentValue - self.purchasePrice)/self.purchasePrice)*100
        durationYears = (date.today() - self.purchaseDate).days/365
        if durationYears==0:
            return 0
        else:
            return percentChange/durationYears

