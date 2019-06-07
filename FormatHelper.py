"""
Author: Don Claveau
Create Date: 5/19/2019
Description: This script has helper functions for parsing and formatting values
Updates:

"""
from datetime import date,timedelta,datetime

def DateFromMmddyyyyString(mmddyyyyString):
    '''function to get date from string'''
    format_str = '%m/%d/%Y' # The date format
    datetime_obj = datetime.strptime(mmddyyyyString, format_str)    
    return datetime_obj.date()

def DateFromYyyyMmDdString(yyyymmddString):
    '''function to get date from string'''
    format_str = '%Y-%m-%d' # The date format
    datetime_obj = datetime.strptime(yyyymmddString, format_str)    
    return datetime_obj.date()

def as_percent(amount):
    '''takes an amount and returns a string formatted as a percent'''
    return '{:,.2f}%'.format(amount)
    
def as_currency(amount):
    '''takes an amount and returns a string formatted as dollars and cents; source: https://stackoverflow.com/a/38464098'''
    if amount >= 0:
            return '${:,.2f}'.format(amount)
    else:
            return '-${:,.2f}'.format(-amount)

