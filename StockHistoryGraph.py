"""
Author: Don Claveau
Create Date: 5/26/2019
Description: Loads stock history into memory and generates a line graph. 
X-axis formatting based on example at https://matplotlib.org/3.1.0/gallery/text_labels_and_annotations/date.html
Updates:

"""
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

def MakeLineGraph(stockHistoryJSONFilePath,lineGraphOutputFilePath):
    '''Make a stock history graph'''

    # load data from json file
    with open(stockHistoryJSONFilePath) as f:
        data = json.load(f)
    
    # get distinct symbols
    distinctSymbols = set([s['Symbol'] for s in data])
        
    # plot the lines
    fig, ax = plt.subplots()
    for sym in distinctSymbols:
        symDates = [d for d in data if d['Symbol']==sym]
        dates,closePrices=[],[]
        for s in symDates:
            dates.append(datetime.datetime.strptime(s['Date'], '%d-%b-%y'))
            closePrices.append(s['Close'])
        ax.plot(dates,closePrices)
    
    # format the ticks
    years = mdates.YearLocator()   # every year
    months = mdates.MonthLocator()  # every month
    years_fmt = mdates.DateFormatter('%Y')
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(years_fmt)
    ax.xaxis.set_minor_locator(months)

    # round to nearest years for x-axis range
    distinctDates = set([datetime.datetime.strptime(s['Date'], '%d-%b-%y') for s in data])
    print (distinctDates)
    datesSorted = sorted(distinctDates)
    print (datesSorted)
    datemin = np.datetime64(datesSorted[0], 'Y')
    datemax = np.datetime64(datesSorted[-1], 'Y') + np.timedelta64(1, 'Y')
    ax.set_xlim(datemin, datemax)

    # format the coords message box
    ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
    ax.format_ydata = lambda x: '$%1.2f' % x  # format the price.
    ax.grid(True)

    # rotates and right aligns the x labels, and moves the bottom of the
    # axes up to make room for them
    fig.autofmt_xdate()

    plt.savefig(lineGraphOutputFilePath)
    plt.show()


directory = 'C:/Users/doncl/OneDrive/Documents/DU Coursework/ICT4370 - Python/Unit8-Visualization/Claveau.Don.Unit8'
stockHistoryJSONFilePath = directory + '/AllStocks.json'
lineGraphOutputFilePath = directory + '/graph.png'

MakeLineGraph(stockHistoryJSONFilePath,lineGraphOutputFilePath)