"""
Author: Don Claveau
Create Date: 5/3/2019
Description: This module contains a class for investors 
Updates:

"""

class Investor():
    _lastId=0

    def __init__(self, id, name,address="",phoneNumber=""):
        self.id = id
        self.name = name
        self.address = address
        self.phoneNumber = phoneNumber

    @classmethod
    def new(cls,name,address="",phoneNumber=""):
        newInvestor = cls(cls._nextId(),name,address,phoneNumber)        
        return newInvestor
    
    @classmethod
    def _nextId(cls):
        '''gets the next available id'''
        Investor._lastId=Investor._lastId+1
        return Investor._lastId