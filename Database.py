"""
Author: Don Claveau
Create Date: 5/15/2019
Description: Handles interaction with database 
Updates:

"""

import sqlite3
from Investor import Investor
from Holding import Holding
from Stock import Stock
from Bond import Bond
from FormatHelper import DateFromYyyyMmDdString

class Database():
    _dbName = 'holdings.db'

    def Execute(self,sqlString):
        conn = sqlite3.connect(self._dbName)        
        cursor = conn.cursor()     
        cursor.execute(sqlString)
        conn.commit()
        conn.close()

    def Initialize(self):
        '''create tables and fill from files'''

        #investor, stock, and bond tables
        sql_create_investor = """ CREATE TABLE IF NOT EXISTS investor (
	                                        investor_id integer PRIMARY KEY,
	                                        name text NOT NULL,
                                            address text NULL,
                                            phoneNumber text NULL
	                                    ); """

        sql_create_holding = """ CREATE TABLE IF NOT EXISTS stock (
	                                        stock_id integer PRIMARY KEY,
	                                        investor_id integer NOT NULL,
                                            SYMBOL text,
                                            NO_SHARES integer,
                                            PURCHASE_PRICE real,
                                            CURRENT_VALUE real,
                                            PURCHASE_DATE text                                            
	                                    ); """
        sql_create_security = """ CREATE TABLE IF NOT EXISTS bond (
	                                        bond_id integer PRIMARY KEY,
	                                        investor_id integer NOT NULL,
                                            SYMBOL text,
                                            NO_SHARES integer,
                                            PURCHASE_PRICE real,
                                            CURRENT_VALUE real,
                                            PURCHASE_DATE text, 
                                            Coupon,
                                            Yield
	                                    ); """
        self.Execute(sql_create_investor)
        self.Execute(sql_create_holding)
        self.Execute(sql_create_security)

    def Insert(self,object):
        '''insert a row to a table based on object type'''
        if (isinstance(object,Investor)):
            sql_insert_investor = f"""
                INSERT OR REPLACE INTO investor VALUES(
                    {object.id},
                    '{object.name}',
                    '{object.phoneNumber}',
                    '{object.address}'
                )
            """
            self.Execute(sql_insert_investor)
            return
        if (isinstance(object,Holding)):
            if (isinstance(object.stock,Bond)):
                sql_insert_bond = f"""
                    INSERT OR REPLACE INTO bond VALUES(
                        {object.purchaseId},
                        '{object.investor.id}',
                        '{object.stock.symbol}',
                        '{object.quantity}',
                        '{object.purchasePrice}',
                        '{object.stock.currentValue}',
                        '{object.purchaseDate}',                        
                        '{object.stock.coupon}',
                        '{object.stock.bondYield}'                          
                    )
                """
                self.Execute(sql_insert_bond)
            else:
                sql_insert_stock = f"""
                    INSERT OR REPLACE INTO stock VALUES(
                        {object.purchaseId},
                        '{object.investor.id}',
                        '{object.stock.symbol}',
                        '{object.quantity}',
                        '{object.purchasePrice}',
                        '{object.stock.currentValue}',
                        '{object.purchaseDate}'                        
                    )
                """
                self.Execute(sql_insert_stock)

    def GetHoldings(self):
        sql_select_holdings = """
            SELECT i.investor_id,i.name,i.address,i.phoneNumber,
            'stock',
            stock_id as id,SYMBOL,NO_SHARES,PURCHASE_PRICE,CURRENT_VALUE,PURCHASE_DATE,null,null
            FROM stock s
            INNER JOIN investor i
            UNION
            SELECT i.investor_id,i.name,i.address,i.phoneNumber,
            'bond',
            bond_id as id,SYMBOL,NO_SHARES,PURCHASE_PRICE,CURRENT_VALUE,PURCHASE_DATE,Coupon,Yield
            FROM bond b
            INNER JOIN investor i
        """
        conn = sqlite3.connect(Database._dbName)
        cursor = conn.execute(sql_select_holdings)
        holdings = []
        for row in cursor:
            investor = Investor(row[0],row[1],row[2],row[3])
            purchaseDate = DateFromYyyyMmDdString(row[10])
            if row[4]=="bond":
                stock = Bond(row[6],float(row[9]),float(row[11]),float(row[12]))
            else:
                stock = Stock(row[6],float(row[9]))
            thisHolding=Holding(row[5],investor,stock,int(row[7]),float(row[8]),purchaseDate)
            holdings.append(thisHolding)
        return holdings
