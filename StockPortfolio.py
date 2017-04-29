import random
import csv
import sys
import os
import pip
import time
print(pip.pep425tags.get_supported())
from lxml import html
from lxml import etree
import requests
import pandas as pd
import scipy
import datetime
#import pandas.io.data as web
import matplotlib.pyplot as plt
import seaborn as sns
#from matplotlib import style

from matplotlib.pyplot import *
#from matplotlib import pyplot as plt
from pathlib import Path
#style.use('ggplot')
import numpy as np
#pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1500)
import operator

import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import pandas as pd
from random import randrange
#root = Tk()
#root.resizable(width=False, height=False)
#menu = Menu(root)
#root.config(menu=menu)

'''
menubar = Menu(root)
root.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=False)
#editMenu = Menu(menubar, tearoff=False)

menubar.add_cascade(label="File",underline=0, menu=fileMenu)
#menubar.add_cascade(label="Edit",underline=0, menu=editMenu)

fileMenu.add_command(label="Open...", underline=0)
fileMenu.add_command(label="Save", underline=0)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", underline=1)

'''

#dates = pd.date_range('20160101', periods=6)
#df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))

#root = Tk()

'''
t1 = Text(root)

t1.grid()
'''
#from Tkinter import Tk


def flush(self):
    pass

'''
#If enabled prints Stockportfolio Data to another window
class PrintToT1(object):
 def write(self, s):
     t1.insert(END, s)
     flush(self)

#sys.stdout = PrintToT1()
'''




'''
subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
#
toolbar = Frame(root, bg="blue")

#Status bar
#status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
#status.pack(side=BOTTOM, fill=X)

'''

'''
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)
'''

#theLabel = Label(root, text="This is too easy")
#theLabel.pack()


########################
#Read data from stocks.csv and personal_data.csv
########################

print('Reading data from files...')
script_dir = os.path.dirname(os.path.realpath('__file__'))
print(script_dir)
target_file = os.path.join(script_dir, '..')
print(target_file)
os.chdir(target_file)
retval = os.getcwd()
print(retval)
target_file = os.path.join(retval, 'data\stocks.csv')
target_file2 = os.path.join(retval, 'data\personal_data.csv')
print(target_file2)
os.chdir(retval)
if os.path.isfile(target_file) and os.access(target_file, os.R_OK):
    print('File stocks.csv exists and is readable')
    print('File personal_data.csv exists and is readable')
else:
    print('Either file stocks.csv is missing or is not readable')
    print('Either file personal_data.csv is missing or is not readable')
    sys.exit()
stocksfile = pd.read_csv(target_file)
personal_data_file = pd.read_csv(target_file2)


#row_count = sum(1 for line in personal_data_file)
#print(row_count)

#pd.read_csv(stocksfile)
#df.Col2.str.get_dummies(sep="http").values.sum()


#number_of_stocks = 6

#stocks.csv
stock_name = stocksfile.Stock
buy_price_recommendations = stocksfile.BuyUnder
low_price = stocksfile.LowPrice
high_price = stocksfile.HighPrice
sales_target = stocksfile.SalesTarget
max_pers_of_investments = stocksfile.MaxPersOfInvestments
amount = stocksfile.Amount
gav_kurs = stocksfile.GavKurs
stock_currency = stocksfile.Currency
stock_web_page = stocksfile.StockWebPage

#personal_data.csv
name = personal_data_file.AttributeValue[0]
debt = personal_data_file.AttributeValue[1]
debt_interest_rate = personal_data_file.AttributeValue[2]
cash_account1 = personal_data_file.AttributeValue[3]
cash_account2 = personal_data_file.AttributeValue[4]
other_investments = personal_data_file.AttributeValue[5]
goldonz = personal_data_file.AttributeValue[6]
minimumbuy = personal_data_file.AttributeValue[7]
currency = personal_data_file.AttributeValue[8]
stocks_max_pers_of_investments = personal_data_file.AttributeValue[9]
number_of_stocks = personal_data_file.AttributeValue[10]
debtfloat = float(debt)
debt_interest_ratefloat = float(debt_interest_rate)
goldonzfloat = float(goldonz)
cash_account1_float = float(cash_account1)
cash_account2_float = float(cash_account2)
cashfloat = cash_account1_float + cash_account2_float
minimumbuyfloat = float(minimumbuy)
other_investmentsfloat = float(other_investments)
stocks_max_pers_of_investments_float = float(stocks_max_pers_of_investments)
number_of_stocks_int = int(number_of_stocks)
pers_bank_require_downpayment_for_loan = personal_data_file.AttributeValue[11]
current_est_value_apartment = personal_data_file.AttributeValue[12]
monthly_loan_payments = float(personal_data_file.AttributeValue[13])


#Stock name
name_list = []
for x in range(0, number_of_stocks_int):
    name_list = name_list + [stock_name[x]]

#Buy price recommendations
buy_price_recommendations_list = []
for x in range(0, number_of_stocks_int):
    buy_price_recommendations_list = buy_price_recommendations_list + [buy_price_recommendations[x]]

low_price_list = []
for x in range(0, number_of_stocks_int):
    low_price_list = low_price_list + [low_price[x]]

high_price_list = []
for x in range(0, number_of_stocks_int):
    high_price_list = high_price_list + [high_price[x]]

#Sales target
sales_target_list = []
for x in range(0, number_of_stocks_int):
    sales_target_list = sales_target_list + [sales_target[x]]


#Amount
amount_list = []
for x in range(0, number_of_stocks_int):
    amount_list = amount_list + [amount[x]]


#Max allowed percentage to own of investments
max_pers_of_investments_list = []
for x in range(0, number_of_stocks_int):
    max_pers_of_investments_list = max_pers_of_investments_list + [max_pers_of_investments[x]]


#Purchase rate GAV from Nordnet
gav_kurs_list = []
for x in range(0, number_of_stocks_int):
    gav_kurs_list = gav_kurs_list + [gav_kurs[x]]


#Currency of the stock
stock_currency_list = []
for x in range(0, number_of_stocks_int):
    stock_currency_list = stock_currency_list + [stock_currency[x]]


########################
#Exchange rates
########################

def returnexchangerate(xecurrencywebpage):
    page = requests.get(xecurrencywebpage)
    tree = html.fromstring(page.content)
    rate = tree.xpath('//*[@id="ucc-container"]/span[2]/span[2]/text()')
    ratestr = ''.join(rate)
    exchangeratefloat = float(ratestr.replace(',', '.'))
    return exchangeratefloat

'''
def returnexchangerate(xecurrencywebpage, from_currency):
    currency
    page = requests.get(xecurrencywebpage)
    tree = html.fromstring(page.content)
    rate = tree.xpath('//*[@id="ucc-container"]/span[2]/span[2]/text()')
    ratestr = ''.join(rate)
    exchangeratefloat = float(ratestr.replace(',', '.'))
    return exchangeratefloat
'''
cadsekratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1&From=CAD&To=SEK')
usdsekratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1&From=USD&To=SEK')
cadeurratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?From=EUR&To=CAD')


#Gold Price svd.se
def returngoldusd():
    goldpage = requests.get('https://bors-nliv.svd.se/')
    goldtree = html.fromstring(goldpage.content)
    goldrate = goldtree.xpath('normalize-space(//*[@id="indicatorbox"]/ul/li[2]/ul/li[2]/span[1]/text())')
    #goldchange = goldtree.xpath('// *[ @ id = "indicatorbox"] / ul / li[2] / ul / li[2] / span[2]/text()')
    #goldchange = goldtree.xpath('//*[@id="indicatorbox"]/ul/li[2]/ul/li[2]/span[2]/text()')
    goldchange = goldtree.xpath('normalize-space(//*[@id="indicatorbox"]/ul/li[2]/ul/li[2]/span[2]/text())')
    #print(goldchange)
    str1 = goldchange.find(' ')
    #print(str1)

    '''
    if ' ' in goldchange:
        goldchangeshort = goldchange[:goldchange.index(' ')+1]
        print(goldchangeshort)
    '''
    #goldchangestr = ''.join(goldrate)
    #print(goldchangestr)
    #goldchangestr

    goldratestr = ''.join(goldrate)
    goldratefloat = float(goldratestr.replace(' ', ''))
    return goldratefloat


'''
no_exchange_rate = 1
if stock_currency_list[x] == 'CAD':
    exchange_rate_to_use = cadsekratefloat
elif stock_currency_list[x] == 'USD':
        exchange_rate_to_use = usdsekratefloat
else stock_currency_list[x] == 'SEK':
    exchange_rate_to_use = no_exchange_rate
    
    
def choose_exchange_rate(stock_currency_list[x]):
    if stock_currency_list[x] == 'CAD':
        exchange_rate_to_use = cadsekratefloat
        return exchange_rate_to_use
    elif stock_currency_list[x] == 'USD':
        exchange_rate_to_use = usdsekratefloat
        return exchange_rate_to_use
    else stock_currency_list[x] == 'SEK':
        exchange_rate_to_use = no_exchange_rate
        return exchange_rate_to_use
'''


########################
#Stock prices
########################

#Stock current price
def stockcurrentpricebloomberg(bloombergwebpage):
    page = requests.get(bloombergwebpage)
    tree = html.fromstring(page.content)
    price = tree.xpath('//*[@id="content"]/div/div/div[1]/div/div[4]/div[2]/text()')
    pricestr = ''.join(price)
    stockcurrentpricebloombergfloat = float(pricestr)
    return stockcurrentpricebloombergfloat

'''
#Stock current price Nordnet
def stockcurrentpricenordnet(nordnetwebpage):
    page = requests.get(nordnetwebpage)
    tree = html.fromstring(page.content)
    change = tree.xpath('//*[@id="instrumentcontainer"]/div/table/tr/td[3]/text()')
    print(change)
    changestr = ''.join(change)
    print(changestr)
    stockcurrentpricenordnetfloat = float(changestr)
    return stockcurrentpricenordnetfloat
'''

stock_current_pricefloat_list = []
for x in range(0, number_of_stocks_int):
    stock_current_pricefloat_list = stock_current_pricefloat_list + [(stockcurrentpricebloomberg(stock_web_page[x]))]


#Stock previous close price Bloomberg
def previousstockclose(bloombergwebpage):
    page = requests.get(bloombergwebpage)
    tree = html.fromstring(page.content)
    change = tree.xpath('//*[@id="content"]/div/div/div[8]/div/div/div[4]/div[2]/text()')
    changestr = ''.join(change)
    previousstockclosefloat = float(changestr)
    return previousstockclosefloat

'''
#Stock previous close price Nordnet
def previousstockclosenordnet(nordnetwebpage):
    page = requests.get(nordnetwebpage)
    tree = html.fromstring(page.content)
    change = tree.xpath('//*[@id="instrumentcontainer"]/div/table/tr/td[3]')
    changestr = ''.join(change)
    previousstockclosenordnetfloat = float(changestr)
    return previousstockclosenordnetfloat
'''

previous_stock_closefloat_list = []
for x in range(0, number_of_stocks_int):
    previous_stock_closefloat_list = previous_stock_closefloat_list + [(previousstockclose(stock_web_page[x]))]

#Calculations

cash_in_apartment = float(current_est_value_apartment) - float(debt)

max_loan_cash = int(current_est_value_apartment) - ((int(pers_bank_require_downpayment_for_loan) / 100) * int(current_est_value_apartment))

how_much_more_loan_possible = max_loan_cash - float(debt)

#Change % from previous stock close to current stock price
def laststockpricechange(previousstockclose, currentstockprice):
    change = 100 * (currentstockprice - previousstockclose) / previousstockclose
    return change

#Value of Gold
goldusd = returngoldusd()
goldsek = returngoldusd() * usdsekratefloat
gold = goldsek * goldonzfloat

#Total Current Value of stock
def stockvalue(amount, pricefloat, ratefloat):
    return amount*pricefloat*ratefloat


'''
for x in range(0, number_of_stocks):
    stockvalue_list = stockvalue_list + [stockvalue[x]]

'''
stock_currency_list = []
for x in range(0, number_of_stocks_int):
    stock_currency_list = stock_currency_list + [stock_currency[x]]

stock_exchangerate_from_list = []
for x in range(0, number_of_stocks_int):
    stock_exchangerate_from_list = stock_exchangerate_from_list + [stock_currency[x] + currency]

stock_exchangerate_list = []
for x in range(0, number_of_stocks_int):
    stock_exchangerate_list = stock_exchangerate_list + [returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1&From=' + stock_exchangerate_from_list[x] + '&To=' + currency + '')]

print(stock_exchangerate_from_list)
print(stock_exchangerate_list)


stockvalue_list = []
for x in range(0, number_of_stocks_int):
    stockvalue_list = stockvalue_list + [stockvalue(amount_list[x], stock_current_pricefloat_list[x], stock_exchangerate_list[x])]


# Daily % change in stock value
stock_daily_change_pers_list = []
for x in range(0, number_of_stocks_int):
    stock_daily_change_pers_list = stock_daily_change_pers_list + [laststockpricechange(previous_stock_closefloat_list[x], stock_current_pricefloat_list[x])]


stock_paid_list = []
for x in range(0, number_of_stocks_int):
    stock_paid_list = stock_paid_list + [stockvalue(gav_kurs[x], amount_list[x], stock_exchangerate_list[x])]


#Difference in price, current value - paid value
def stockdifference(totalvalue, totalpaid):
    return totalvalue-totalpaid


stock_diff_list = []
for x in range(0, number_of_stocks_int):
    stock_diff_list = stock_diff_list + [stockdifference(stockvalue_list[x], stock_paid_list[x])]

# Daily % change in stock value
total_change_list = []
for x in range(0, number_of_stocks_int):
    total_change_list = total_change_list + [(100 * stock_diff_list[x] / stock_paid_list[x])]

# Stocks percentage of all investments
def investmentpercentage(investment, sumofinvestments):
    return 100*investment/sumofinvestments

#Sum of all stocks difference in price
allstocksdifference = sum(stock_diff_list)

#Total sum of all stocks paid value
total_stocks_paid_value = sum(stock_paid_list)

#Total sum of current value of all stocks
sumofallstocks_list = []
for x in range(0, number_of_stocks_int):
    sumofallstocks_list = sumofallstocks_list + [stockvalue_list[x]]

sumofallstocks = sum(sumofallstocks_list)

#Total sum of all investments
sumofinvestments = cashfloat + sumofallstocks + gold + other_investmentsfloat


net_worth = cash_in_apartment + sumofinvestments

#Stock previous close value
stock_previous_close_value_list = []
for x in range(0, number_of_stocks_int):
    stock_previous_close_value_list = stock_previous_close_value_list + [stockvalue(previous_stock_closefloat_list[x], amount_list[x], stock_exchangerate_list[x])]

total_stocks_close_value = sum(stock_previous_close_value_list)

#Stock development today
daily_portfolio_development = 100 * (sumofallstocks - total_stocks_close_value) / total_stocks_close_value

#Commodity's Percentage of investments
cashpercentage = investmentpercentage(cashfloat, sumofinvestments)
goldpercentage = investmentpercentage(gold, sumofinvestments)
stockspercentage = investmentpercentage(sumofallstocks, sumofinvestments)
otherinvestmentspercentage = investmentpercentage(other_investmentsfloat, sumofinvestments)

percentage_list = []
for x in range(0, number_of_stocks_int):
    percentage_list = percentage_list + [investmentpercentage(stockvalue_list[x], sumofinvestments)]

#Total % change, all stocks
total_change = 100 * allstocksdifference / total_stocks_paid_value

########################
#Algorithms
########################

#Buy Algorithm
def stock_buy(maxpersofinvestment, percentage, currprice, buyunder, cashfloat, minimumbuyfloat): #stockspercentage, stocks_max_pers_of_investments_float):
    if  minimumbuyfloat > cashfloat:
        buy = False
    else:
        if currprice >= buyunder:
            buy = False
        else:
            if percentage > maxpersofinvestment:
                buy = False
                '''else:
                if sumofallstocks > stocks_max_pers_of_investments_float:
                   buy = False'''
            else:
                buy = True
    return buy



buy_recommendation_list = []
for x in range(0, number_of_stocks_int):
    buy_recommendation_list = buy_recommendation_list + [stock_buy(max_pers_of_investments[x], percentage_list[x],
                              stock_current_pricefloat_list[x], buy_price_recommendations[x], cashfloat,
                              minimumbuyfloat)] #, stockspercentage, stocks_max_pers_of_investments)]


########################
#Text based GUI
########################
'''
percentage_list = []
for x in range(0, number_of_stocks):
    percentage_list = percentage_list + [investmentpercentage(stockvalue_list[x], sumofinvestments)]

def sort_table(table, cols):
    for col in reversed(cols):
        table = sorted(table, key=operator.itemgetter(col))
    return table
'''
#df.style.highlight_null().render().split('\n')[:10]
#df = df.sort_values(by=[stock_alph_order, stock_ranking_list], ascending=[False,True])



def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = 'red' if val < 0 else 'black'
    return 'color: %s' % color

def highlight_max(data, color='yellow'):

    attr = 'background-color: {}'.format(color)
    if data.ndim == 1:  # Series from .apply(axis=0) or axis=1
        is_max = data == data.max()
        return [attr if v else '' for v in is_max]
    else:  # from .apply(axis=None)
        is_max = data == data.max().max()
        return pd.DataFrame(np.where(is_max, attr, ''),
                            index=data.index, columns=data.columns)

#s = df.style.applymap(color_negative_red)
#print(s)
#Printing
print('--------------------------------------------------------------------------------')
print('************ Welcome to Stock Portfolio,', name, '************')
print('--------------------------------------------------------------------------------')
print('Canadian/Swedish exchange rate, 1 CAD =', cadsekratefloat, 'SEK')
print('USD/Swedish exchange rate, 1 USD =', usdsekratefloat, 'SEK')
print('Canadian/Euro exchange rate, 1 CAD =', cadeurratefloat, 'EUR')
print('Current Gold rate', goldusd, '$/Onz,','%.2f' % goldsek, 'SEK/Onz')
print('--------------------------------------------------------------------------------')
print("Debt", debt, currency)
print("Debt Interest rate", debt_interest_rate, '%')
print("Minimum buy", minimumbuyfloat, currency)
print("Cash in Account 1:", cash_account1_float, currency)
print("Cash in Account 2:", cash_account2_float, currency)
print("All available Cash", cashfloat, currency)
print("Other Investments", other_investmentsfloat, currency)
print("Gold", '%.2f' % gold, currency)
print("Sum of all stocks", '%.2f' % sumofallstocks, currency)
print("Sum of all stocks paid", '%.2f' % total_stocks_paid_value, currency)
print("All stocks difference", '%.2f' % allstocksdifference, currency)
print("Sum of all investments", '%.2f' % sumofinvestments, currency)
print("Stock Portfolio development today", '%.2f' % daily_portfolio_development, '%')
print('--------------------------------------------------------------------------------')
print("Cash percentage of investments", '%.2f' % cashpercentage, '%')
print("Gold percentage of investments", '%.2f' % goldpercentage, '%')
print("Stocks percentage of investments", '%.2f' % stockspercentage, '%')
print("Other Investments percentage of investments", '%.2f' % otherinvestmentspercentage, '%')
print('--------------------------------------------------------------------------------')
print("Time updated: ", time.ctime())
print('--------------------------------------------------------------------------------')
#print(s)
#df.style.apply(highlight_max, color='darkorange', axis=None)
#print(df)

########################
#Spreadsheet GUI
########################

class Stocktable(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        #self.PersonalData1()
        self.CreateUIStock()
        self.LoadStockTable()
        #self.LoadStockTableColor()
        self.CreateUISummary()
        self.LoadSummaryTable()
        self.CreateUIPersonalData()
        self.PersonalData()

        #Tkinter Grid Geometry Manager. Defines how to expand the widget if the resulting cell is larger than the widget itself.
        self.grid(sticky = (N,S,W,E))
        #self.returnexchangerate()
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)
        #parent.grid_rowconfigure(1, height=200)

    def PersonalData1(self):
        self.parent.grid_rowconfigure(0,weight=1)
        self.parent.grid_columnconfigure(0,weight=1)
        self.parent.config(background="lavender")

        # Define the different GUI widgets
        self.dose_label = tkinter.Label(self.parent, text = "Dose:")
        self.dose_entry = tkinter.Entry(self.parent)
        self.dose_label.grid(row = 0, column = 0, sticky = tkinter.W)
        self.dose_entry.grid(row = 0, column = 1)

        self.modified_label = tkinter.Label(self.parent, text = "Date Modified:")
        self.modified_entry = tkinter.Entry(self.parent)
        self.modified_label.grid(row = 1, column = 0, sticky = tkinter.W)
        self.modified_entry.grid(row = 1, column = 1)


    def CreateUIStock(self):
        tv = Treeview(self)
        tv['columns'] = ('currprice', 'prevclose', 'daychangepers', 'buyunder', 'lowprice', 'highprice', 'recommendedbuy', 'amount', 'gav', 'persofinvestment',
                         'maxpersofinvestment', 'paidvalue', 'totalvalue', 'difference', 'totalchange', 'selltarget')
        tv.heading("#0", text='Stock', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('currprice', text='Current Price')
        tv.column('currprice', anchor='center', width=80)
        tv.heading('prevclose', text='Previous Close')
        tv.column('prevclose', anchor='center', width=80)
        tv.heading('daychangepers', text='Day Change %')
        tv.column('daychangepers', anchor='center', width=80)
        tv.heading('buyunder', text='Buy Under')
        tv.column('buyunder', anchor='center', width=50)
        tv.heading('lowprice', text='Low Price')
        tv.column('lowprice', anchor='center', width=50)
        tv.heading('highprice', text='High Price')
        tv.column('highprice', anchor='center', width=50)
        tv.heading('recommendedbuy', text='Rec Buy')
        tv.column('recommendedbuy', anchor='center', width=50 ,)
        tv.heading('amount', text='Amount')
        tv.column('amount', anchor='center', width=50)
        tv.heading('gav', text='Average paid GAV')
        tv.column('gav', anchor='center', width=80)
        tv.heading('persofinvestment', text='% of Investments')
        tv.column('persofinvestment', anchor='center', width=50)
        tv.heading('maxpersofinvestment', text='Max % of Inv')
        tv.column('maxpersofinvestment', anchor='center', width=50)
        tv.heading('paidvalue', text='Paid Value')
        tv.column('paidvalue', anchor='center', width=80)
        tv.heading('totalvalue', text='Total Value')
        tv.column('totalvalue', anchor='center', width=80)
        tv.heading('difference', text='Difference')
        tv.column('difference', anchor='center', width=80)
        tv.heading('totalchange', text='Total Change %')
        tv.column('totalchange', anchor='center', width=80)
        tv.heading('selltarget', text='Sell Target')
        tv.column('selltarget', anchor='center', width=50)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        #self.grid_rowconfigure(10, weight = 10)
        #self.grid_columnconfigure(0, weight = 1)

    def CreateUISummary(self):
        tv = Treeview(self)
        tv['columns'] = ('currprice', 'prevclose', 'daychangepers', 'buyunder', 'recommendedbuy', 'amount', 'gav',
                         'persofinvestment', 'maxpersofinvestment', 'paidvalue', 'totalvalue', 'difference', 'totalchange', 'selltarget')
        tv.heading("#0", text='Summary', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('currprice', text='')
        tv.column('currprice', anchor='center', width=150)
        tv.heading('prevclose', text='')
        tv.column('prevclose', anchor='center', width=100)
        tv.heading('daychangepers', text='Day Change')
        tv.column('daychangepers', anchor='center', width=120)
        tv.heading('buyunder', text='')
        tv.column('buyunder', anchor='center', width=100)
        tv.heading('recommendedbuy', text='')
        tv.column('recommendedbuy', anchor='center', width=80)
        tv.heading('amount', text='')
        tv.column('amount', anchor='center', width=80)
        tv.heading('gav', text='')
        tv.column('gav', anchor='center', width=100)
        tv.heading('persofinvestment', text='Stocks % of Invs')
        tv.column('persofinvestment', anchor='center', width=100)
        tv.heading('maxpersofinvestment', text='Stocks Max % of Invs')
        tv.column('maxpersofinvestment', anchor='center', width=100)
        tv.heading('paidvalue', text='Stocks Paid Value')
        tv.column('paidvalue', anchor='center', width=100)
        tv.heading('totalvalue', text='Stocks Total Value')
        tv.column('totalvalue', anchor='center', width=100)
        tv.heading('difference', text='Stocks Difference')
        tv.column('difference', anchor='center', width=100)
        tv.heading('totalchange', text='Stocks Total Change %')
        tv.column('totalchange', anchor='center', width=100)
        tv.heading('selltarget', text='')
        tv.column('selltarget', anchor='center', width=100)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)


    def LoadStockTable(self):
        '''
        self.labels = []
        style = ttk.Style()
        style.configure("red.TLabel", background='red')
        style.configure("green.TLabel", background='green')
        style.configure("header.TLabel", font = '-weight bold')
        for x in range(0, number_of_stocks_int):
           self.labels.append('', 'end',
                                 text=stock_name[x], values=(
                                 '%.2f' % stock_current_pricefloat_list[x] + ' ' + stock_currency[x],
                                 '%.2f' % previous_stock_closefloat_list[x] + ' ' + stock_currency[x],
                                 '%.2f' % stock_daily_change_pers_list[x] +
                                 ' %', '%.2f' % buy_price_recommendations_list[x] + ' ' + stock_currency[x],
                                 '%.2f' % low_price_list[x] + ' ' + stock_currency[x],
                                 buy_recommendation_list[x],
                                 amount_list[x],
                                 '%.2f' % gav_kurs_list[x] + ' ' + stock_currency[x],
                                 '%.2f' % percentage_list[x] +
                                 ' %', '%.2f' % max_pers_of_investments_list[x] + ' %',
                                 '%.2f' % stock_paid_list[x] + ' ' + currency,
                                 '%.2f' % stockvalue_list[x] + ' ' + currency,
                                 '%.2f' % stock_diff_list[x] + ' ' + currency,
                                 '%.2f' % total_change_list[x] + ' %',
                                 sales_target[x]))
        '''



        

        for x in range(0, number_of_stocks_int):
            self.treeview.insert('', 'end',
                                 text=stock_name[x], values=(
                                 '%.2f' % stock_current_pricefloat_list[x] + ' ' + stock_currency[x],
                                 '%.2f' % previous_stock_closefloat_list[x] + ' ' + stock_currency[x],
                                 '%.2f' % stock_daily_change_pers_list[x] +
                                 ' %', '%.2f' % buy_price_recommendations_list[x] + ' ' + stock_currency[x],
                                 '%.2f' % low_price_list[x] + ' ' + stock_currency[x],
                                 '%.2f' % high_price_list[x] + ' ' + stock_currency[x],
                                 buy_recommendation_list[x],
                                 amount_list[x],
                                 '%.2f' % gav_kurs_list[x] + ' ' + stock_currency[x],
                                 '%.2f' % percentage_list[x] +
                                 ' %', '%.2f' % max_pers_of_investments_list[x] + ' %',
                                 '%.2f' % stock_paid_list[x] + ' ' + currency,
                                 '%.2f' % stockvalue_list[x] + ' ' + currency,
                                 '%.2f' % stock_diff_list[x] + ' ' + currency,
                                 '%.2f' % total_change_list[x] + ' %',
                                 sales_target[x]))
        '''

        '''    
        ttk.Style().configure("Treeview", background="white",
                              foreground="black", fieldbackground="white")
        

        #ttk.Style().configure("Treeview", background="firebrick1")

        '''
        print(ttk.Style().theme_names())
        ttk.Style().theme_use('default')
        ttk.Style().configure("Treeview", background="#383838", foreground="green")
        ttk.Style().configure("Treeview.Heading", background="green", foreground="blue")
        '''

    '''
    def LoadStockTableColor(self):
        self.table = GridView(self)
        self.table.pack()
        self.table.set(new_rand_df())
    '''

    def LoadSummaryTable(self):

        #ttk.Style().configure("Treeview", background="#636363", foreground="white")
        self.treeview.insert('', 'end', text='', values=('', '', '%.2f' % daily_portfolio_development +
                                                         ' %', '', '', '', '', '%.2f' % stockspercentage +
                                                         ' %', stocks_max_pers_of_investments +
                                                         ' %',  '%.2f' % total_stocks_paid_value + ' ' + currency,
                                                         '%.2f' % sumofallstocks + ' ' + currency,
                                                         '%.2f' % allstocksdifference + ' ' + currency,
                                                         '%.2f' % total_change + ' %', ''))
        self.treeview.insert('', 'end', text='Canadian/Swedish exchange rate', values=(
        '1 CAD = ' + '%f' % cadsekratefloat + ' ' + currency, '', '', '', '', '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='Canadian/USD exchange rate', values=(
        '1 USD = ' + '%f' % usdsekratefloat + ' ' + currency, '', '', '', '', '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='Canadian/Euro exchange rate', values=(
        '1 CAD = ' + '%f' % cadeurratefloat + ' ' + currency, '', '', '', '', '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='Current Gold rate', values=(
        '%.2f' % goldsek + ' SEK/Onz', '', '', '', '', '', '', '', '', '', '', '', ''))


        self.treeview.insert('', 'end', text='Cash percentage of investments', values=(
        '%.2f' % cashpercentage + '%', '', '', '', '', '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='Gold percentage of investments', values=(
        '%.2f' % goldpercentage + '%', '', '', '', '', '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='Stocks percentage of investments', values=(
        '%.2f' % stockspercentage + '%', '', '', '', '', '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='Other percentage of investments', values=(
        '%.2f' % otherinvestmentspercentage + '%', '', '', '', '', '', '', '', '', '', '', '', ''))
        #text = self.Text(root, selectbackground="red", inactiveselectbackground="blue")
        #text.pack()
        #style = ttk.Style()
        #ttk.Style().configure("Treeview", background="#383838", foreground="white", fieldbackground="red")
        #self.ttk.Combobox().pack()
        #self.tag_configure('oddrow', background='orange')
        #self.tag_configure('evenrow', background='purple')


    def CreateUIPersonalData(self):
        tv = Treeview(self)
        tv['columns'] = ('currprice', 'prevclose', 'daychangepers', 'buyunder', 'recommendedbuy', 'amount', 'gav',
                         'persofinvestment', 'maxpersofinvestment', 'paidvalue', 'totalvalue', 'difference', 'totalchange', 'selltarget')
        tv.heading("#0", text='Personal data', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('currprice', text='')
        tv.column('currprice', anchor='center', width=100)
        tv.heading('prevclose', text='')
        tv.column('prevclose', anchor='center', width=230)
        tv.heading('daychangepers', text='')
        tv.column('daychangepers', anchor='center', width=100)
        tv.heading('buyunder', text='')
        tv.column('buyunder', anchor='center', width=100)
        tv.heading('recommendedbuy', text='')
        tv.column('recommendedbuy', anchor='center', width=100)
        tv.heading('amount', text='')
        tv.column('amount', anchor='center', width=100)
        tv.heading('gav', text='')
        tv.column('gav', anchor='center', width=100)
        tv.heading('persofinvestment', text='')
        tv.column('persofinvestment', anchor='center', width=100)
        tv.heading('maxpersofinvestment', text='')
        tv.column('maxpersofinvestment', anchor='center', width=100)
        tv.heading('paidvalue', text='')
        tv.column('paidvalue', anchor='center', width=100)
        tv.heading('totalvalue', text='')
        tv.column('totalvalue', anchor='center', width=100)
        tv.heading('difference', text='')
        tv.column('difference', anchor='center', width=150)
        tv.heading('totalchange', text='')
        tv.column('totalchange', anchor='center', width=100)
        tv.heading('selltarget', text='')
        tv.column('selltarget', anchor='center', width=100)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def PersonalData(self):
        self.treeview.insert('', 'end', text='Minimum buy', values=(
        '%.f' % minimumbuyfloat + ' ' + currency, 'Loan', debt + ' ' + currency, '', '', '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='Cash in Account 1', values=(
        '%.f' % cash_account1_float + ' ' + currency, 'Debt Interest rate', debt_interest_rate + ' %', '', '', '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='Cash in Account 2', values=(
        '%.f' % cash_account2_float + ' ' + currency, 'Required % banks require paid for apart', pers_bank_require_downpayment_for_loan + ' %', '', '', '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='All available Cash', values=(
        '%.f' % cashfloat + ' ' + currency, 'Max amount of cash you can get, apartment', '%.f' % max_loan_cash + ' ' + currency, '', '', '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='Gold', values=(
        '%.f' % gold + ' ' + currency, 'How much more loan possible', '%.f' % how_much_more_loan_possible + ' ' + currency, '', '', '', '', '', '', '', '', 'Last Updated', ''))
        self.treeview.insert('', 'end', text='Other Investments', values=(
        '%.f' % other_investmentsfloat + ' ' + currency, 'Estimated apartment value', current_est_value_apartment + ' ' + currency, '', '', '', '', '', '', '', '', time.ctime(), ''))
        self.treeview.insert('', 'end', text='Sum of all investments', values=(
        '%.f' % sumofinvestments + ' ' + currency, 'Cash in apartment', '%.f' % cash_in_apartment + ' ' + currency, '', '', '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='Net worth', values=(
        '%.f' % net_worth  + ' ' + currency, 'Monthly loan payment', '%.f' % monthly_loan_payments + ' ' + currency, '', '', '', '', '', '', '', '', '', ''))


'''   class Piechart(Frame):
        def __init__(self, parent):
            self.Pie()

        def Pie(self):
'''

'''
PADDING = dict(padx=3, pady=3)
class GridView(Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.labels = []
        style = ttk.Style()
        style.configure("red.TLabel", background='red')
        style.configure("green.TLabel", background='green')
        style.configure("header.TLabel", font = '-weight bold')

    def set(self, df):
        self.clear()
        for col, name in enumerate(df.columns):
            lbl = ttk.Label(self, text=name, style='header.TLabel')
            lbl.grid(row=0, column=col, **PADDING)
            self.labels.append(lbl)

        for row, values in enumerate(df.itertuples(), 1):
            for col, value in enumerate(values[1:]):
                lbl = ttk.Label(self, text=value, style=self.get_style(value))
                lbl.grid(row=row, column=col, **PADDING)
                self.labels.append(lbl)


def new_rand_df():
    width = 10
    height = 10
    return pd.DataFrame([[randrange(100) for _ in range(width)] for _ in range(height)],
                        columns=list('abcdefghijklmnopqrstuvwxyz'[:width]))

'''
def piechart():
    labels = 'Gold', 'Cash', 'Stocks', 'Other Investments'
    sizes = [gold, cashfloat, sumofallstocks, other_investmentsfloat]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0, 0, 0.1, 0)  # explode Stocks

    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%3.2f%%', shadow=True, startangle=90)
    plt.title("Investments")
    plt.axis('equal')
    #fig = pyplot.gcf()
    #fig.canvas.set_window_title('My title')
    plt.show()

def piechart_inc_apartment():
    labels = 'Gold', 'Cash', 'Stocks', 'Other Investments', 'Cash in Apartment'
    sizes = [gold, cashfloat, sumofallstocks, other_investmentsfloat, cash_in_apartment]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'brown']
    explode = (0, 0, 0, 0, 0.1)  # explode Stocks

    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%3.2f%%', shadow=True, startangle=90)
    plt.title("Investments, including cash in apartment")
    plt.axis('equal')
    #fig = pyplot.gcf()
    #fig.canvas.set_window_title('My title')
    plt.show()

def my_stocks():
    stocks_tk = Tk()
    stocks_tk.title("My Stocks")
    stocks_tk.grid_rowconfigure(0, weight=1)
    stocks_tk.grid_columnconfigure(0, weight=1)
    stocks_tk.config(background="lightblue")

    stocks_tk.name_label = tkinter.Label(stocks_tk, text="Name:")
    stocks_tk.buy_under_label = tkinter.Label(stocks_tk, text="Buy Under:")
    stocks_tk.low_price_label = tkinter.Label(stocks_tk, text="Low Price:")
    stocks_tk.high_price_label = tkinter.Label(stocks_tk, text="High Price:")
    stocks_tk.amount_label = tkinter.Label(stocks_tk, text="Amount:")
    stocks_tk.gav_label = tkinter.Label(stocks_tk, text="GAV:")
    stocks_tk.currency_label = tkinter.Label(stocks_tk, text="Currency:")
    stocks_tk.max_pers_of_investments_label = tkinter.Label(stocks_tk, text="Max % of Investments:")
    stocks_tk.stock_web_page_label = tkinter.Label(stocks_tk, text="Stock Web Page:")
    stocks_tk.sell_target_label = tkinter.Label(stocks_tk, text="Sell Target:")

    stocks_tk.name_label.grid(row=0, column=0, sticky=tkinter.W)
    stocks_tk.buy_under_label.grid(row=0, column=1, sticky=tkinter.W)
    stocks_tk.low_price_label.grid(row=0, column=2, sticky=tkinter.W)
    stocks_tk.high_price_label.grid(row=0, column=2, sticky=tkinter.W)
    stocks_tk.amount_label.grid(row=0, column=3, sticky=tkinter.W)
    stocks_tk.gav_label.grid(row=0, column=4, sticky=tkinter.W)
    stocks_tk.currency_label.grid(row=0, column=5, sticky=tkinter.W)
    stocks_tk.max_pers_of_investments_label.grid(row=0, column=6, sticky=tkinter.W)
    stocks_tk.stock_web_page_label.grid(row=0, column=7, sticky=tkinter.W)
    stocks_tk.sell_target_label.grid(row=0, column=8, sticky=tkinter.W)


    stocks_tk.entry_list = []
    for x in range(0, 8):
        stocks_tk.stock_name_entry = tkinter.Entry(stocks_tk)
        stocks_tk.stock_name_entry.insert(x, stock_name[x])
        stocks_tk.stock_name_entry.grid(row=x+1, column=0)

        stocks_tk.buy_price_recommendations_entry = tkinter.Entry(stocks_tk)
        stocks_tk.buy_price_recommendations_entry.insert(x, buy_price_recommendations_list[x])
        stocks_tk.buy_price_recommendations_entry.grid(row=x+1, column=1)

        stocks_tk.low_price_entry = tkinter.Entry(stocks_tk)
        stocks_tk.low_price_entry.insert(x, low_price_list[x])
        stocks_tk.low_price_entry.grid(row=x+1, column=2)

        stocks_tk.high_price_entry = tkinter.Entry(stocks_tk)
        stocks_tk.high_price_entry.insert(x, high_price_list[x])
        stocks_tk.high_price_entry.grid(row=x+1, column=2)

        stocks_tk.amount_entry = tkinter.Entry(stocks_tk)
        stocks_tk.amount_entry.insert(x, amount_list[x])
        stocks_tk.amount_entry.grid(row=x+1, column=3)

        stocks_tk.gav_kurs_entry = tkinter.Entry(stocks_tk)
        stocks_tk.gav_kurs_entry.insert(x, gav_kurs_list[x])
        stocks_tk.gav_kurs_entry.grid(row=x+1, column=4)

        stocks_tk.currency_entry = tkinter.Entry(stocks_tk)
        stocks_tk.currency_entry.insert(x, stock_currency[x])
        stocks_tk.currency_entry.grid(row=x+1, column=5)

        stocks_tk.max_pers_of_investments_entry = tkinter.Entry(stocks_tk)
        stocks_tk.max_pers_of_investments_entry.insert(x, max_pers_of_investments_list[x])
        stocks_tk.max_pers_of_investments_entry.grid(row=x+1, column=6)

        stocks_tk.stock_web_page_entry = tkinter.Entry(stocks_tk)
        stocks_tk.stock_web_page_entry.insert(x, stock_web_page[x])
        stocks_tk.stock_web_page_entry.grid(row=x+1, column=7)

        stocks_tk.sales_target_entry = tkinter.Entry(stocks_tk)
        stocks_tk.sales_target_entry.insert(x, sales_target_list[x])
        stocks_tk.sales_target_entry.grid(row=x+1, column=8)

        stocks_tk.save_button = tkinter.Button(stocks_tk, text="Save", command=donothing)
        stocks_tk.save_button.grid(row=x+2, column=8, sticky=tkinter.W)

'''
    
    
    max_pers_of_investments
    amount
    gav_kurs
    stock_currency
    stock_web_page
'''

'''
    stocks_tk.debt_label = tkinter.Label(stocks_tk, text="Debt:")
    stocks_tk.debt_entry = tkinter.Entry(stocks_tk)
    stocks_tk.debt_entry.insert(10, debtfloat)
    stocks_tk.debt_label.grid(row=1, column=0, sticky=tkinter.W)
    stocks_tk.debt_entry.grid(row=1, column=1)
'''
    #stocks_tk.grid()

def personal_data():
    personal = Tk()
    #e1 = Entry(personal)
    #namefield = e1.get()
    personal.title("Personal Data")
    personal.grid_rowconfigure(0, weight=1)
    personal.grid_columnconfigure(0, weight=1)
    #personal.parent.geometry("1000x1000")
    personal.config(background="lightblue")
    #personal.treeview.insert('', 'end', text='hgjhgjkghjghj', values=(
    #    '%.2f' % cashpercentage + '%', '', '', '', '', '', '', '', '', '', '', '', ''))
    #personal.pack()

    '''
    personal.name_entry.insert('', 'end', values=(personal.name_entry.get()))
    personal.debt_entry.insert(10, debtfloat)
    personal.debt_interest_rate_entry.insert(10, debt_interest_ratefloat)
    personal.cash_account1_entry.insert(10, cash_account1_float)
    personal.cash_account2_entry.insert(10, cash_account2_float)
    personal.other_investments_entry.insert(10, other_investmentsfloat)
    personal.gold_in_onz_entry.insert(10, goldonzfloat)
    personal.minimum_buy_entry.insert(10, minimumbuyfloat)
    personal.currency_entry.insert(10, currency)
    personal.max_pers_of_investments_entry.insert(10, stocks_max_pers_of_investments_float)
    personal.number_of_stocks_entry.insert(10, number_of_stocks_int)
    '''


    personal.name_label = tkinter.Label(personal, text="Name:")
    personal.name_entry = tkinter.Entry(personal)
    personal.name_entry.insert(10, name)
    personal.name_label.grid(row=0, column=0, sticky=tkinter.W)
    personal.name_entry.grid(row=0, column=1)

    personal.debt_label = tkinter.Label(personal, text="Debt:")
    personal.debt_entry = tkinter.Entry(personal)
    personal.debt_entry.insert(10, debtfloat)
    personal.debt_label.grid(row=1, column=0, sticky=tkinter.W)
    personal.debt_entry.grid(row=1, column=1)

    personal.debt_interest_rate_label = tkinter.Label(personal, text="Debt interest rate:")
    personal.debt_interest_rate_entry = tkinter.Entry(personal)
    personal.debt_interest_rate_entry.insert(10, debt_interest_ratefloat)
    personal.debt_interest_rate_label.grid(row=2, column=0, sticky=tkinter.W)
    personal.debt_interest_rate_entry.grid(row=2, column=1)

    personal.cash_account1_label = tkinter.Label(personal, text="Cash Account 1:")
    personal.cash_account1_entry = tkinter.Entry(personal)
    personal.cash_account1_entry.insert(10, cash_account1_float)
    personal.cash_account1_label.grid(row=3, column=0, sticky=tkinter.W)
    personal.cash_account1_entry.grid(row=3, column=1)

    personal.cash_account2_label = tkinter.Label(personal, text="Cash Account 2:")
    personal.cash_account2_entry = tkinter.Entry(personal)
    personal.cash_account2_entry.insert(10, cash_account2_float)
    personal.cash_account2_label.grid(row=4, column=0, sticky=tkinter.W)
    personal.cash_account2_entry.grid(row=4, column=1)

    personal.other_investments_label = tkinter.Label(personal, text="Other Investments:")
    personal.other_investments_entry = tkinter.Entry(personal)
    personal.other_investments_entry.insert(10, other_investmentsfloat)
    personal.other_investments_label.grid(row=5, column=0, sticky=tkinter.W)
    personal.other_investments_entry.grid(row=5, column=1)

    personal.gold_in_onz_label = tkinter.Label(personal, text="Gold in Onz:")
    personal.gold_in_onz_entry = tkinter.Entry(personal)
    jee = personal.gold_in_onz_entry.get()
    #print(jee)
    personal.gold_in_onz_entry.insert(10, goldonzfloat)
    personal.gold_in_onz_label.grid(row=6, column=0, sticky=tkinter.W)
    personal.gold_in_onz_entry.grid(row=6, column=1)

    personal.minimum_buy_label = tkinter.Label(personal, text="Minimum Buy:")
    personal.minimum_buy_entry = tkinter.Entry(personal)
    personal.minimum_buy_entry.insert(10, minimumbuyfloat)
    personal.minimum_buy_label.grid(row=7, column=0, sticky=tkinter.W)
    personal.minimum_buy_entry.grid(row=7, column=1)

    personal.currency_label = tkinter.Label(personal, text="Currency:")
    personal.currency_entry = tkinter.Entry(personal)
    personal.currency_entry.insert(10, currency)
    personal.currency_label.grid(row=8, column=0, sticky=tkinter.W)
    personal.currency_entry.grid(row=8, column=1)

    personal.max_pers_of_investments_label = tkinter.Label(personal, text="Stocks Max Procent of investments:")
    personal.max_pers_of_investments_entry = tkinter.Entry(personal)
    personal.max_pers_of_investments_entry.insert(10, stocks_max_pers_of_investments_float)
    personal.max_pers_of_investments_label.grid(row=9, column=0, sticky=tkinter.W)
    personal.max_pers_of_investments_entry.grid(row=9, column=1)

    personal.number_of_stocks_label = tkinter.Label(personal, text="Number of stocks:")
    personal.number_of_stocks_entry = tkinter.Entry(personal)
    personal.number_of_stocks_entry.insert(10, number_of_stocks_int)
    personal.number_of_stocks_label.grid(row=10, column=0, sticky=tkinter.W)
    personal.number_of_stocks_entry.grid(row=10, column=1)

    personal.save_button = tkinter.Button(personal, text="Save", command=write_personal_data(personal))
    personal.save_button.grid(row=11, column=1, sticky=tkinter.W)

    personal.grid()


'''
class personal_data(tkinter.Frame):

    def __init__(self, parent):

        tkinter.Frame.__init__(self, parent)
        self.parent=parent
        self.initialize_user_interface()

    def initialize_user_interface(self):
        """Draw a user interface allowing the user to type
        items and insert them into the treeview
        """
        self.parent.title("Canvas Test")
        self.parent.grid_rowconfigure(0,weight=1)
        self.parent.grid_columnconfigure(0,weight=1)
        self.parent.config(background="lavender")


        # Define the different GUI widgets
        self.dose_label = tkinter.Label(self.parent, text = "Dose:")
        self.dose_entry = tkinter.Entry(self.parent)
        self.dose_label.grid(row = 0, column = 0, sticky = tkinter.W)
        self.dose_entry.grid(row = 0, column = 1)

        self.modified_label = tkinter.Label(self.parent, text = "Date Modified:")
        self.modified_entry = tkinter.Entry(self.parent)
        self.modified_label.grid(row = 1, column = 0, sticky = tkinter.W)
        self.modified_entry.grid(row = 1, column = 1)

        self.submit_button = tkinter.Button(self.parent, text = "Insert", command = self.insert_data)
        self.submit_button.grid(row = 2, column = 1, sticky = tkinter.W)
        self.exit_button = tkinter.Button(self.parent, text = "Exit", command = self.parent.quit)
        self.exit_button.grid(row = 0, column = 3)

        # Set the treeview
        self.tree = ttk.Treeview( self.parent, columns=('Dose', 'Modification date'))
        self.tree.heading('#0', text='Item')
        self.tree.heading('#1', text='Dose')
        self.tree.heading('#2', text='Modification Date')
        self.tree.column('#1', stretch=tkinter.YES)
        self.tree.column('#2', stretch=tkinter.YES)
        self.tree.column('#0', stretch=tkinter.YES)
        self.tree.grid(row=4, columnspan=4, sticky='nsew')
        self.treeview = self.tree
        # Initialize the counter
        self.i = 0


    def insert_data(self):
        """
        Insertion method.
        """
        self.treeview.insert('', 'end', text="Item_"+str(self.i), values=(self.dose_entry.get()+" mg", self.modified_entry.get()))
        # Increment counter
        self.i = self.i + 1
'''

def donothing():
    filewin = Toplevel()
    button = Button(filewin, text="Do nothing button")
    button.pack()

def quit():
    sys.exit(0)

def write_personal_data(personal):
    with open(r'C:\Users\JannePC-Skylake\PycharmProjects\StockPortfolio\data\try.csv', 'w') as csvfile:
        fieldnames = ['PersonalAttribute', 'AttributeValue']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'PersonalAttribute': 'name', 'AttributeValue': personal.name_entry.get()})
        writer.writerow({'PersonalAttribute': 'debt', 'AttributeValue': personal.debt_entry.get()})
        writer.writerow({'PersonalAttribute': 'debt_interest_rate', 'AttributeValue': personal.debt_interest_rate_entry.get()})
        writer.writerow({'PersonalAttribute': 'cash_account1', 'AttributeValue': personal.cash_account1_entry.get()})
        writer.writerow({'PersonalAttribute': 'cash_account2', 'AttributeValue': personal.cash_account2_entry.get()})
        writer.writerow({'PersonalAttribute': 'other_investments', 'AttributeValue': personal.other_investments_entry.get()})
        writer.writerow({'PersonalAttribute': 'goldonz', 'AttributeValue': personal.gold_in_onz_entry.get()})
        writer.writerow({'PersonalAttribute': 'minimumbuy', 'AttributeValue': personal.minimum_buy_entry.get()})
        writer.writerow({'PersonalAttribute': 'currency', 'AttributeValue': personal.currency_entry.get()})
        writer.writerow({'PersonalAttribute': 'stock_max_pers_of_investments', 'AttributeValue': personal.max_pers_of_investments_entry.get()})
        writer.writerow({'PersonalAttribute': 'number_of_stocks', 'AttributeValue': personal.number_of_stocks_entry.get()})

'''
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
'''


def main():

    #Creates main window
    root = Tk()
    #root.resizable(width=False, height=False) #If this is enabled, then you cannot adjust the size of main window
    root.wm_title("Stock Portfolio")
    Stocktable(root)

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)



    filemenu.add_command(label="Personal Data", command=personal_data)
    filemenu.add_command(label="My Stocks", command=my_stocks)
    '''
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_command(label="Save as...", command=donothing)
    filemenu.add_command(label="Close", command=donothing)
    filemenu.add_separator()
    '''
    filemenu.add_command(label="Exit", command=quit)
    menubar.add_cascade(label="Settings", menu=filemenu)

    '''
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=donothing)
    editmenu.add_separator()
    editmenu.add_command(label="Cut", command=donothing)
    editmenu.add_command(label="Copy", command=donothing)
    editmenu.add_command(label="Paste", command=donothing)
    editmenu.add_command(label="Delete", command=donothing)
    editmenu.add_command(label="Select All", command=donothing)
    menubar.add_cascade(label="Edit", menu=editmenu)
    '''

    '''
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)
    '''

    graphmenu = Menu(menubar, tearoff=0)
    graphmenu.add_command(label="Investments Chart - Pie Diagram", command=piechart)
    graphmenu.add_command(label="Investments Chart + cash in apartment - Pie Diagram", command=piechart_inc_apartment)
    menubar.add_cascade(label="Graphs", menu=graphmenu)

    root.config(menu=menubar)

    root.mainloop()

if __name__ == '__main__':
    main()

