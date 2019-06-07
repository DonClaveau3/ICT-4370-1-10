"""
Author: Don Claveau
Create Date: 5/3/2019
Description: This module contains a class for bonds 
Updates:

"""
from Stock import Stock

class Bond(Stock):
    def __init__(self,symbol,currentValue,coupon,bondYield):
        Stock.__init__(self,symbol,currentValue)
        self.coupon=coupon
        self.bondYield = bondYield

    def print_bondDescription(self):
        '''prints a summary of the bond'''
        print(self.symbol)
        print("Coupon: "+self.coupon)
        print("Yield: "+self.bondYield)
        