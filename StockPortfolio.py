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
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import datetime


import numpy as np
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1500)
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import pandas as pd
from random import randrange

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
target_file3 = os.path.join(retval, 'data\kryptos.csv')
print(target_file)
print(target_file2)
print(target_file3)
os.chdir(retval)
if os.path.isfile(target_file) and os.access(target_file, os.R_OK):
    print('File stocks.csv exists and is readable')
    print('File personal_data.csv exists and is readable')
    print('File kryptos.csv exists and is readable')
else:
    print('Either file stocks.csv is missing or is not readable')
    print('Either file personal_data.csv is missing or is not readable')
    print('Either file kryptos.csv is missing or is not readable')
    sys.exit()
stocksfile = pd.read_csv(target_file)
personal_data_file = pd.read_csv(target_file2)
kryptosfile = pd.read_csv(target_file3)

#stocks.csv
stock_name = stocksfile.Stock
buy_price_recommendations = stocksfile.BuyUnder
low_price = stocksfile.LowPrice
high_price = stocksfile.HighPrice
sales_target = stocksfile.SalesTarget
stock_max_pers_of_investments = stocksfile.MaxPersOfInvestments
stock_amount = stocksfile.Amount
stock_gav_kurs = stocksfile.GavKurs
stock_currency = stocksfile.Currency
stock_web_page = stocksfile.StockWebPage

#kryptos.csv
krypto_name = kryptosfile.Krypto
#krypto_buy_price_recommendations = kryptosfile.BuyUnder
#krypto_low_price = kryptosfile.LowPrice
#krypto_high_price = kryptosfile.HighPrice
#krypto_sales_target = kryptosfile.SalesTarget
krypto_amount = kryptosfile.KryptoAmount
krypto_max_pers_of_investments = kryptosfile.KryptoMaxAllowedPersofInv
krypto_gav_kurs = kryptosfile.KryptoAveragePaid
krypto_currency = kryptosfile.Currency
krypto_web_page = kryptosfile.KryptoWebPage

#personal_data.csv
name = personal_data_file.AttributeValue[0]
debt = personal_data_file.AttributeValue[1]
debt_interest_rate = personal_data_file.AttributeValue[2]
cash_account1 = personal_data_file.AttributeValue[3]
cash_account2 = personal_data_file.AttributeValue[4]
loan_given = personal_data_file.AttributeValue[5]
cash_in_apartment3 = personal_data_file.AttributeValue[6]
other_investments = personal_data_file.AttributeValue[7]
goldonz = personal_data_file.AttributeValue[8]
minimumbuy = personal_data_file.AttributeValue[9]
currency = personal_data_file.AttributeValue[10]
stock_total_max_pers_of_investments = personal_data_file.AttributeValue[11]
number_of_stocks = personal_data_file.AttributeValue[12]
debtfloat = float(debt)
debt_interest_ratefloat = float(debt_interest_rate)
goldonzfloat = float(goldonz)
cash_account1_float = float(cash_account1)
cash_account2_float = float(cash_account2)
cashfloat = cash_account1_float + cash_account2_float
loan_given_float = float(loan_given)

minimumbuyfloat = float(minimumbuy)
other_investmentsfloat = float(other_investments)
#stock_max_pers_of_investments_float = float(stock_max_pers_of_investments)

number_of_stocks_int = int(number_of_stocks)

pers_bank_require_downpayment_for_loan = personal_data_file.AttributeValue[13]
current_est_value_apartment = personal_data_file.AttributeValue[14]
monthly_loan_payments = float(personal_data_file.AttributeValue[15])
cash_in_apartment2_float = float(personal_data_file.AttributeValue[16])
monthly_salary = float(personal_data_file.AttributeValue[17])
annual_salary = float(personal_data_file.AttributeValue[18])
dollar_goal = float(personal_data_file.AttributeValue[19])
number_of_kryptos = personal_data_file.AttributeValue[20]
krypto_total_max_pers_of_investments = personal_data_file.AttributeValue[21]
print(krypto_max_pers_of_investments)
number_of_kryptos_int = int(number_of_kryptos)
print(number_of_kryptos_int)
#krypto_max_pers_of_investments_float = float(krypto_max_pers_of_investments)

#Stock name
name_list = []
for x in range(0, number_of_stocks_int):
    name_list = name_list + [stock_name[x]]

#Krypto name
krypto_name_list = []
for x in range(0, number_of_kryptos_int):
    krypto_name_list = krypto_name_list + [krypto_name[x]]

#Buy price recommendations
buy_price_recommendations_list = []
for x in range(0, number_of_stocks_int):
    buy_price_recommendations_list = buy_price_recommendations_list + [buy_price_recommendations[x]]

'''
#Krypto Buy price recommendations
krypto_buy_price_recommendations_list = []
for x in range(0, number_of_kryptos_int):
    krypto_buy_price_recommendations_list = krypto_buy_price_recommendations_list + [krypto_buy_price_recommendations[x]]
'''
low_price_list = []
for x in range(0, number_of_stocks_int):
    low_price_list = low_price_list + [low_price[x]]

'''
#Krypto low price list
krypto_low_price_list = []
for x in range(0, number_of_kryptos_int):
    krypto_low_price_list = krypto_low_price_list + [krypto_low_price[x]]
'''

high_price_list = []
for x in range(0, number_of_stocks_int):
    high_price_list = high_price_list + [high_price[x]]

'''
#Krypto high price list
krypto_high_price_list = []
for x in range(0, number_of_kryptos_int):
    krypto_high_price_list = krypto_high_price_list + [krypto_high_price[x]]
'''

#Sales target
sales_target_list = []
for x in range(0, number_of_stocks_int):
    sales_target_list = sales_target_list + [sales_target[x]]

'''
#Sales target krypto
krypto_sales_target_list = []
for x in range(0, number_of_kryptos_int):
    krypto_sales_target_list = krypto_sales_target_list + [krypto_sales_target[x]]
'''

#Amount
stock_amount_list = []
for x in range(0, number_of_stocks_int):
    stock_amount_list = stock_amount_list + [stock_amount[x]]

#Krypto Amount
krypto_amount_list = []
for x in range(0, number_of_kryptos_int):
    krypto_amount_list = krypto_amount_list + [krypto_amount[x]]


#Max allowed percentage to own of Stock investments
stock_max_pers_of_investments_list = []
for x in range(0, number_of_stocks_int):
    stock_max_pers_of_investments_list = stock_max_pers_of_investments_list + [stock_max_pers_of_investments[x]]

#Max allowed percentage to own of Krypto investments
krypto_max_pers_of_investments_list = []
for x in range(0, number_of_kryptos_int):
    krypto_max_pers_of_investments_list = krypto_max_pers_of_investments_list + [krypto_max_pers_of_investments[x]]


#Purchase rate GAV from Nordnet
stock_gav_kurs_list = []
for x in range(0, number_of_stocks_int):
    stock_gav_kurs_list = stock_gav_kurs_list + [stock_gav_kurs[x]]

#Purchase rate GAV
krypto_gav_kurs_list = []
for x in range(0, number_of_kryptos_int):
    krypto_gav_kurs_list = krypto_gav_kurs_list + [krypto_gav_kurs[x]]


#Currency of the stock
stock_currency_list = []
for x in range(0, number_of_stocks_int):
    stock_currency_list = stock_currency_list + [stock_currency[x]]


#Currency of the krypto
krypto_currency_list = []
for x in range(0, number_of_kryptos_int):
    krypto_currency_list = krypto_currency_list + [krypto_currency[x]]


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

cadsekratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1&From=CAD&To=SEK')
usdsekratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1&From=USD&To=SEK')
phpsekratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1&From=PHP&To=SEK')
cadeurratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1?From=CAD&To=EUR')
usdeurratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1?From=USD&To=EUR')

sekcadratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1&From=SEK&To=CAD')
sekusdratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1&From=SEK&To=USD')
sekphpratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1&From=SEK&To=PHP')
eurcadratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1?From=EUR&To=CAD')
eurusdratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1&From=EUR&To=USD')


cash_in_apartment3_float1 = float(cash_in_apartment3)
cash_in_apartment3_float = cash_in_apartment3_float1 * phpsekratefloat

#('//*[@id="content"]/div/div/div[1]/div/div[4]/div[2]/text()')
#//*[@id="content"]/div/div/div[3]/div[3]/div/table/tbody/tr[1]/td[3]
#//*[@id="indicatorbox"]/ul/li[2]/ul/li[2]/span[1]
#Gold Price svd.se
def returngoldusd():
    goldpage = requests.get('https://bors-nliv.svd.se/')
    #goldpage = requests.get('https://www.bloomberg.com/markets/commodities/futures/metals')
    goldtree = html.fromstring(goldpage.content)
    #print(goldtree)
    goldrate = goldtree.xpath('normalize-space(//*[@id="indicatorbox"]/ul/li[2]/ul/li[2]/span[1]/text())')
    #goldrate = goldtree.xpath('normalize-space(//*[@id="content"]/div/div/div[3]/div[3]/div/tr[1]/td[3]/text())')
    #goldrate = goldtree.xpath('normalize-space(//*[@id="content"]/div/div/div[3]/div[3]/div/tr[1]/text())')
    #print(goldrate)
    goldratestr = ''.join(goldrate)
    print(goldratestr)
    #exchangeratefloat = float(ratestr.replace(',', '.'))
    #goldratefloat = float(goldratestr.replace(',', ''))
    goldratefloat = float(goldratestr.replace(' ', ''))
    return goldratefloat

def returngoldusdchangepers():
    goldpage = requests.get('https://bors-nliv.svd.se/index.php/ravaror')
    #goldpage = requests.get('https://www.bloomberg.com/markets/commodities/futures/metals')
    goldtree = html.fromstring(goldpage.content)
    #print(goldtree)
    goldrate = goldtree.xpath('//*[@id="72831"]/td[3]/span[1]/text()')
    #goldrate = goldtree.xpath('normalize-space(//*[@id="content"]/div/div/div[3]/div[3]/div/tr[1]/td[3]/text())')
    #goldrate = goldtree.xpath('normalize-space(//*[@id="content"]/div/div/div[3]/div[3]/div/tr[1]/text())')
    print(goldrate)
    goldratestr = ''.join(goldrate)
    print(goldratestr)
    #exchangeratefloat = float(ratestr.replace(',', '.'))
    #goldratefloat = float(goldratestr.replace(',', ''))
    replaceminus = goldratestr.replace('−', '-')
    goldratechangepersfloat = float(replaceminus.replace(',', '.'))
    print(goldratechangepersfloat)
    return goldratechangepersfloat

#Oil Price svd.se
def returnoilusd():
    oilpage = requests.get('https://bors-nliv.svd.se/')
    oiltree = html.fromstring(oilpage.content)
    print(oiltree)
    oilrate = oiltree.xpath('normalize-space(//*[@id="indicatorbox"]/ul/li[2]/ul/li[1]/span[1]/text())')
    print(oilrate)
    oilratestr = ''.join(oilrate)
    print(oilratestr)
    oilratefloat = float(oilratestr.replace(',', '.'))
    print(oilratefloat)
    return oilratefloat

def returnoilusdchangepers():
    oilpage = requests.get('https://bors-nliv.svd.se/index.php/ravaror')
    #goldpage = requests.get('https://www.bloomberg.com/markets/commodities/futures/metals')
    oiltree = html.fromstring(oilpage.content)
    #print(goldtree)
    oilrate = oiltree.xpath('//*[@id="42051"]/td[3]/span[1]/text()')
    #goldrate = goldtree.xpath('normalize-space(//*[@id="content"]/div/div/div[3]/div[3]/div/tr[1]/td[3]/text())')
    #goldrate = goldtree.xpath('normalize-space(//*[@id="content"]/div/div/div[3]/div[3]/div/tr[1]/text())')
    print(oilrate)
    oilratestr = ''.join(oilrate)
    print(oilratestr)
    #exchangeratefloat = float(ratestr.replace(',', '.'))
    #goldratefloat = float(goldratestr.replace(',', ''))
    replaceminus = oilratestr.replace('−', '-')
    oilratechangepersfloat = float(replaceminus.replace(',', '.'))
    print(oilratechangepersfloat)
    return oilratechangepersfloat

def returngoldusdgdx():
    goldgdxpage = requests.get('http://www.nasdaq.com/symbol/gdx')
    goldgdxtree = html.fromstring(goldgdxpage.content)
    #print(goldtree)
    goldgdxrate = goldgdxtree.xpath('//*[@id="qwidget_lastsale"]/text()')
    #print(goldgdxrate)
    goldgdxratestr = ''.join(goldgdxrate)
    print(goldgdxratestr)
    goldgdxratefloat = float(goldgdxratestr.replace('$', ''))
    return goldgdxratefloat

def returngoldusdgdxperschange():
    goldgdxperschangepage = requests.get('http://www.nasdaq.com/symbol/gdx')
    goldgdxperschangetree = html.fromstring(goldgdxperschangepage.content)
    #print(goldtree)
    goldgdxperschangerate = goldgdxperschangetree.xpath('//*[@id="qwidget_percent"]/text()')
    print(goldgdxperschangerate)
    goldgdxperschangeratestr = ''.join(goldgdxperschangerate)
    print(goldgdxperschangeratestr)
    replaceminus = goldgdxperschangeratestr.replace('−', '-')
    goldgdxperschangeratefloat = float(replaceminus.replace('%', ''))
    print(goldgdxperschangeratefloat)
    return goldgdxperschangeratefloat

def returngoldusdgdxj():
    goldgdxjpage = requests.get('http://www.nasdaq.com/symbol/gdxj')
    goldgdxjtree = html.fromstring(goldgdxjpage.content)
    #print(goldtree)
    goldgdxjrate = goldgdxjtree.xpath('//*[@id="qwidget_lastsale"]/text()')
    #print(goldgdxjrate)
    goldgdxjratestr = ''.join(goldgdxjrate)
    print(goldgdxjratestr)
    goldgdxjratefloat = float(goldgdxjratestr.replace('$', ''))
    return goldgdxjratefloat

def returngoldusdgdxjperschange():
    goldgdxjperschangepage = requests.get('http://www.nasdaq.com/symbol/gdxj')
    goldgdxjperschangetree = html.fromstring(goldgdxjperschangepage.content)
    #print(goldtree)
    goldgdxjperschangerate = goldgdxjperschangetree.xpath('//*[@id="qwidget_percent"]/text()')
    print(goldgdxjperschangerate)
    goldgdxjperschangeratestr = ''.join(goldgdxjperschangerate)
    print(goldgdxjperschangeratestr)
    replaceminus = goldgdxjperschangeratestr.replace('−', '-')
    goldgdxjperschangeratefloat = float(replaceminus.replace('%', ''))
    print(goldgdxjperschangeratefloat)
    return goldgdxjperschangeratefloat


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

stock_current_pricefloat_list = []  
for x in range(0, number_of_stocks_int):
    stock_current_pricefloat_list = stock_current_pricefloat_list + [(stockcurrentpricebloomberg(stock_web_page[x]))]

#Krypto current price
def kryptocurrentprice(kryptowebpage):
    print("kryptowebpage: ", kryptowebpage)
    page = requests.get(kryptowebpage)
    print("page: ", page)
    tree = html.fromstring(page.content)
    print("tree: ", tree)
    price = tree.xpath('//span[@id="quote_price"]/text()')
    print("Price: ", price)
    pricestr = ''.join(price)
    print("Pricestr: ", pricestr)
    pricefloat = float(pricestr.replace('$', ' '))
    print("pricefloat: ", pricefloat)
    return pricefloat

#krypto_current_pricefloat_list
krypto_current_pricefloat_list = []
for x in range(0, number_of_kryptos_int):
    krypto_current_pricefloat_list = krypto_current_pricefloat_list + [(kryptocurrentprice(krypto_web_page[x]))]
    #stock_current_pricefloat_list = stock_current_pricefloat_list + [(stockcurrentpricebloomberg(stock_web_page[x]))]

#Stock previous close price Bloomberg
def previousstockclose(bloombergwebpage):
    page = requests.get(bloombergwebpage)
    tree = html.fromstring(page.content)
    change = tree.xpath('//*[@id="content"]/div/div/div[8]/div/div/div[4]/div[2]/text()')
    changestr = ''.join(change)
    previousstockclosefloat = float(changestr)
    return previousstockclosefloat

previous_stock_closefloat_list = []
for x in range(0, number_of_stocks_int):
    previous_stock_closefloat_list = previous_stock_closefloat_list + [(previousstockclose(stock_web_page[x]))]

#Krypto previous close price
#def previouskryptoclose(kryptowebpage):
    #page = requests.get(bloombergwebpage)
    #tree = html.fromstring(page.content)
    #change = tree.xpath('//*[@id="content"]/div/div/div[8]/div/div/div[4]/div[2]/text()')
    #changestr = '3'
    #changestr = ''.join(change)
    #previouskryptoclosefloat = float(changestr)
    #return previouskryptoclosefloat

    #print("kryptowebpage: ", kryptowebpage)
    #page = requests.get(kryptowebpage)
    #print("page: ", page)
    #tree = html.fromstring(page.content)
    #print("tree: ", tree)
    #price = tree.xpath('//span[@id="quote_price"]/text()')
    #print("Price: ", price)
    #pricestr = ''.join(price)
    #print("Pricestr: ", pricestr)
    #pricefloat = float(pricestr.replace('$', ' '))
    #print("pricefloat: ", pricefloat)
    #return pricefloat

#previous_krypto_closefloat_list = []
#for x in range(0, number_of_kryptos_int):
    #previous_krypto_closefloat_list = previous_krypto_closefloat_list + [(previouskryptoclose(krypto_web_page[x]))]

#Krypto 24h Volume
def krypto24hvolume(kryptowebpage):
    print("kryptowebpage: ", kryptowebpage)
    page = requests.get(kryptowebpage)
    print("page: ", page)
    tree = html.fromstring(page.content)
    print("tree: ", tree)
    krypto24hvolume = tree.xpath('normalize-space(/html/body/div[3]/div/div[1]/div[4]/div[1]/div[2]/div[2]/text())')
    print("krypto24hvolume: ", krypto24hvolume)
    krypto24hvolumestr = ''.join(krypto24hvolume)
    print("Pkrypto24hvolumestr: ", krypto24hvolumestr)
    krypto24hvolumestr1 = krypto24hvolumestr.replace('$', ' ')
    print("krypto24hvolumestr1: ", krypto24hvolumestr1)
    krypto24hvolumefloat = float(krypto24hvolumestr1.replace(',', ''))
    print("krypto24hvolumefloat: ", krypto24hvolumefloat)
    return krypto24hvolumefloat

def krypto24hchangepers(kryptowebpage):
    print("kryptowebpage: ", kryptowebpage)
    page = requests.get(kryptowebpage)
    print("page: ", page)
    tree = html.fromstring(page.content)
    print("tree: ", tree)
    price = tree.xpath('/html/body/div[3]/div/div[1]/div[3]/div[2]/span[2]/text()')
    print("Price: ", price)
    pricestr = ''.join(price)
    print("Pricestr: ", pricestr)
    pricestr1 = pricestr.replace('(', '')
    print("pricestr1: ", pricestr1)
    pricestr2 = pricestr1.replace(')', '')
    print("pricestr2: ", pricestr2)
    pricefloat = float(pricestr2.replace('%', ''))
    print("pricefloat: ", pricefloat)
    return pricefloat

krypto_daily_change_pers_list = []
for x in range(0, number_of_kryptos_int):
    krypto_daily_change_pers_list = krypto_daily_change_pers_list + [(krypto24hchangepers(krypto_web_page[x]))]

krypto24hvolume_list = []
for x in range(0, number_of_kryptos_int):
    krypto24hvolume_list = krypto24hvolume_list + [(krypto24hvolume(krypto_web_page[x]))]

#Calculations

def krypto_24h_price(krypto_current_price, krypto_daily_change_pers):
    krypto_24h_price = krypto_current_price / (1 + (krypto_daily_change_pers/100))
    return krypto_24h_price

krypto_24h_price_list = []
for x in range(0, number_of_kryptos_int):
    krypto_24h_price_list = krypto_24h_price_list + [(krypto_24h_price(krypto_current_pricefloat_list[x], krypto_daily_change_pers_list[x]))]

cash_in_apartment1 = float(current_est_value_apartment) - float(debt)

max_loan_cash = int(current_est_value_apartment) - ((int(pers_bank_require_downpayment_for_loan) / 100) * int(current_est_value_apartment))

how_much_more_loan_possible = max_loan_cash - float(debt)

#Change % from previous stock close to current stock price
def laststockpricechange(previousstockclose, currentstockprice):
    change = 100 * (currentstockprice - previousstockclose) / previousstockclose
    return change

#Change % from previous krypto close to current stock price
def lastkryptopricechange(previouskryptoclose, currentkryptoprice):
    change = 100 * (currentkryptoprice - previouskryptoclose) / previouskryptoclose
    return change

#Value of Gold
goldusd = returngoldusd()
goldsek = returngoldusd() * usdsekratefloat
gold = goldsek * goldonzfloat
goldgdxusd = returngoldusdgdx()
goldgdxperschange = returngoldusdgdxperschange()
goldgdxjusd = returngoldusdgdxj()
goldgdxjperschange = returngoldusdgdxjperschange()

goldusdchangepers = returngoldusdchangepers()
oilusdchangepers = returnoilusdchangepers()



#Value of Oil
oilusd = returnoilusd()
oilsek = returnoilusd() * usdsekratefloat

#Financial goal in SEK
sek_goal = dollar_goal * usdsekratefloat

#Total Current Value of stock
def stockvalue(amount, pricefloat, ratefloat):
    return amount*pricefloat*ratefloat

#Total Current Value of Krypto
def kryptovalue(amount, pricefloat, ratefloat):
    return amount*pricefloat*ratefloat

stock_currency_list = []
for x in range(0, number_of_stocks_int):
    stock_currency_list = stock_currency_list + [stock_currency[x]]

stock_exchangerate_from_list = []
for x in range(0, number_of_stocks_int):
    stock_exchangerate_from_list = stock_exchangerate_from_list + [stock_currency[x] + currency]

krypto_exchangerate_from_list = []
for x in range(0, number_of_kryptos_int):
    krypto_exchangerate_from_list = krypto_exchangerate_from_list + [krypto_currency[x] + currency]

stock_exchangerate_list = []
for x in range(0, number_of_stocks_int):
    stock_exchangerate_list = stock_exchangerate_list + [returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1&From=' + stock_exchangerate_from_list[x] + '&To=' + currency + '')]

krypto_exchangerate_list = []
for x in range(0, number_of_kryptos_int):
    krypto_exchangerate_list = krypto_exchangerate_list + [returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1&From=' + krypto_exchangerate_from_list[x] + '&To=' + currency + '')]
    #krypto_exchangerate_list = krypto_exchangerate_list + [1]

print(stock_exchangerate_from_list)
print(stock_exchangerate_list)


stockvalue_list = []
for x in range(0, number_of_stocks_int):
    stockvalue_list = stockvalue_list + [stockvalue(stock_amount_list[x], stock_current_pricefloat_list[x], stock_exchangerate_list[x])]


kryptovalue_list = []
for x in range(0, number_of_kryptos_int):
    kryptovalue_list = kryptovalue_list + [kryptovalue(krypto_amount_list[x], krypto_current_pricefloat_list[x], krypto_exchangerate_list[x])]
    #kryptovalue_list = kryptovalue_list + [kryptovalue(krypto_amount_list[x], 1, 1)]

# Daily % change in stock value
stock_daily_change_pers_list = []
for x in range(0, number_of_stocks_int):
    stock_daily_change_pers_list = stock_daily_change_pers_list + [laststockpricechange(previous_stock_closefloat_list[x], stock_current_pricefloat_list[x])]

# Daily % change in Krypto value
#krypto_daily_change_pers_list = []
#for x in range(0, number_of_kryptos_int):
    #krypto_daily_change_pers_list = krypto_daily_change_pers_list + [lastkryptopricechange(previous_krypto_closefloat_list[x], krypto_current_pricefloat_list[x])]



stock_paid_list = []
for x in range(0, number_of_stocks_int):
    stock_paid_list = stock_paid_list + [stockvalue(stock_gav_kurs[x], stock_amount_list[x], stock_exchangerate_list[x])]


krypto_paid_list = []
for x in range(0, number_of_kryptos_int):
    krypto_paid_list = krypto_paid_list + [kryptovalue(krypto_gav_kurs[x], krypto_amount_list[x], krypto_exchangerate_list[x])]


#Difference in price, current value - paid value
def stockdifference(totalvalue, totalpaid):
    return totalvalue-totalpaid

#Difference in price, current value - paid value
def kryptodifference(totalvalue, totalpaid):
    return totalvalue-totalpaid

stock_diff_list = []
for x in range(0, number_of_stocks_int):
    stock_diff_list = stock_diff_list + [stockdifference(stockvalue_list[x], stock_paid_list[x])]

krypto_diff_list = []
for x in range(0, number_of_kryptos_int):
    krypto_diff_list = krypto_diff_list + [kryptodifference(kryptovalue_list[x], krypto_paid_list[x])]

# Daily % change in stock value
stock_total_pers_change_list = []
for x in range(0, number_of_stocks_int):
    stock_total_pers_change_list = stock_total_pers_change_list + [(100 * stock_diff_list[x] / stock_paid_list[x])]


# Daily % change in krypto value
krypto_total_pers_change_list = []
for x in range(0, number_of_kryptos_int):
    krypto_total_pers_change_list = krypto_total_pers_change_list + [(100 * krypto_diff_list[x] / krypto_paid_list[x])]


# Commodity percentage of all investments
def investmentpercentage(investment, sumofinvestments):
    return 100*investment/sumofinvestments

#Sum of all stocks difference in price
allstocksdifference = sum(stock_diff_list)

#Sum of all kryptos difference in price
allkryptosdifference = sum(krypto_diff_list)

#Total sum of all stocks paid value
total_stocks_paid_value = sum(stock_paid_list)

#Total sum of all kryptos paid value
total_kryptos_paid_value = sum(krypto_paid_list)

#Total sum of current value of all stocks
sumofallstocks_list = []
for x in range(0, number_of_stocks_int):
    sumofallstocks_list = sumofallstocks_list + [stockvalue_list[x]]

#Total sum of current value of all kryptos
sumofallkryptos_list = []
for x in range(0, number_of_kryptos_int):
    sumofallkryptos_list = sumofallkryptos_list + [kryptovalue_list[x]]

#Total sum of current value of all stocks
sumofallstocks = sum(sumofallstocks_list)
sumofallkryptos = sum(sumofallkryptos_list)

#Total sum of current value of all apartments
sumofallrealestate = cash_in_apartment1 + cash_in_apartment2_float + cash_in_apartment3_float

#Total sum of all investments
sumofinvestments = cashfloat + sumofallstocks + sumofallkryptos + sumofallrealestate + gold + other_investmentsfloat + loan_given_float


net_worth = cash_in_apartment1 + sumofinvestments
missing_from_goal = sek_goal - net_worth

#Stock previous close value
stock_previous_close_value_list = []
for x in range(0, number_of_stocks_int):
    stock_previous_close_value_list = stock_previous_close_value_list + [stockvalue(previous_stock_closefloat_list[x], stock_amount_list[x], stock_exchangerate_list[x])]

#Krypto previous close value
krypto_24h_value_list = []
for x in range(0, number_of_kryptos_int):
    krypto_24h_value_list = krypto_24h_value_list + [kryptovalue(krypto_24h_price_list[x], krypto_amount_list[x], krypto_exchangerate_list[x])]

total_stocks_close_value = sum(stock_previous_close_value_list)
total_kryptos_24h_value = sum(krypto_24h_value_list)

#Stock development today
stocks_daily_portfolio_development = 100 * (sumofallstocks - total_stocks_close_value) / total_stocks_close_value

#Stock development today
kryptos_daily_portfolio_development = 100 * (sumofallkryptos - total_kryptos_24h_value) / total_kryptos_24h_value

#Commodity's Percentage of all investments
cashpercentage = investmentpercentage(cashfloat, sumofinvestments)
goldpercentage = investmentpercentage(gold, sumofinvestments)
stockspercentage = investmentpercentage(sumofallstocks, sumofinvestments)
kryptospercentage = investmentpercentage(sumofallkryptos, sumofinvestments)
cashinapartment1percentage = investmentpercentage(cash_in_apartment1, sumofinvestments)
cashinapartment2percentage = investmentpercentage(cash_in_apartment2_float, sumofinvestments)
cashinapartment3percentage = investmentpercentage(cash_in_apartment3_float, sumofinvestments)
realestatepercentage = investmentpercentage(sumofallrealestate, sumofinvestments)
otherinvestmentspercentage = investmentpercentage(other_investmentsfloat, sumofinvestments)
loangivenspercentage = investmentpercentage(loan_given_float, sumofinvestments)

totalpercentage = cashpercentage + goldpercentage + stockspercentage + kryptospercentage + realestatepercentage + otherinvestmentspercentage + loangivenspercentage

stock_percentage_list = []
for x in range(0, number_of_stocks_int):
    stock_percentage_list = stock_percentage_list + [investmentpercentage(stockvalue_list[x], sumofinvestments)]

krypto_percentage_list = []
for x in range(0, number_of_kryptos_int):
    krypto_percentage_list = krypto_percentage_list + [investmentpercentage(kryptovalue_list[x], sumofinvestments)]

#Total % change, all stocks
stocks_total_change = 100 * allstocksdifference / total_stocks_paid_value

#Total % change, all kryptos
kryptos_total_change = 100 * allkryptosdifference / total_kryptos_paid_value

########################
#Algorithms
########################

#Buy Algorithm
def stock_buy(maxpersofinvestment, percentage, currprice, buyunder, cashfloat, minimumbuyfloat): #stockspercentage, stock_max_pers_of_investments_float):
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

#Buy Algorithm
def krypto_buy(maxpersofinvestment, percentage, currprice, buyunder, cashfloat, minimumbuyfloat): #stockspercentage, stocks_max_pers_of_investments_float):
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
    buy_recommendation_list = buy_recommendation_list + [stock_buy(stock_max_pers_of_investments[x], stock_percentage_list[x],
                              stock_current_pricefloat_list[x], buy_price_recommendations[x], cashfloat,
                              minimumbuyfloat)] #, stockspercentage, stocks_max_pers_of_investments)]

'''
krypto_buy_recommendation_list = []
for x in range(0, number_of_kryptos_int):
    krypto_buy_recommendation_list = krypto_buy_recommendation_list + [krypto_buy(max_pers_of_investments[x], percentage_list[x],
                              krypto_current_pricefloat_list[x], krypto_buy_price_recommendations[x], cashfloat,
                              minimumbuyfloat)] #, stockspercentage, stocks_max_pers_of_investments)]
'''

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
print("Sum of all kryptos", '%.2f' % sumofallkryptos, currency)
print("Sum of all stocks paid", '%.2f' % total_stocks_paid_value, currency)
print("All stocks difference", '%.2f' % allstocksdifference, currency)
print("Sum of all investments", '%.2f' % sumofinvestments, currency)
print("Stock Portfolio development today", '%.2f' % stocks_daily_portfolio_development, '%')
print('--------------------------------------------------------------------------------')
print("Cash percentage of investments", '%.2f' % cashpercentage, '%')
print("Gold percentage of investments", '%.2f' % goldpercentage, '%')
print("Stocks percentage of investments", '%.2f' % stockspercentage, '%')
print("Other Investments percentage of investments", '%.2f' % otherinvestmentspercentage, '%')
print('--------------------------------------------------------------------------------')
print("Time updated: ", time.ctime())
print('--------------------------------------------------------------------------------')

def new_rand_df():
    width = 10
    height = 10
    return pd.DataFrame([[randrange(100) for _ in range(width)] for _ in range(height)],
                        columns=list('abcdefghijklmnopqrstuvwxyz'[:width]))

class StatusBar(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.label.pack(fill=X)

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()

########################
#Spreadsheet GUI
########################

class Kryptotable(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUIKrypto()
        self.LoadKryptoTable()
        #self.CreateUIPersonalData()
        #self.PersonalData()

        #Tkinter Grid Geometry Manager. Defines how to expand the widget if the resulting cell is larger than the widget itself.
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUIKrypto(self):
        tv = Treeview(self)
        tv['columns'] = ('KryptoCurrentPrice', 'Krypto24hPrice', 'Krypto24hChange', 'Krypto24hVol', 'KryptoAmount',
                         'KryptoAveragePaid', 'KryptoPersofinv', 'MaxAllowedPersofInv',
                         'KryptoPaidValue', 'KryptoTotalValue', 'KryptoDiff', 'KryptoTotalChange')
        tv.heading("#0", text='Krypto', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('KryptoCurrentPrice', text='KryptoCurrentPrice')
        tv.column('KryptoCurrentPrice', anchor='center', width=50)
        tv.heading('Krypto24hPrice', text='Krypto24hPrice')
        tv.column('Krypto24hPrice', anchor='center', width=80)
        tv.heading('Krypto24hChange', text='Krypto24hChange')
        tv.column('Krypto24hChange', anchor='center', width=40)
        tv.heading('Krypto24hVol', text='Krypto24hVol')
        tv.column('Krypto24hVol', anchor='center', width=80)
        tv.heading('KryptoAmount', text='KryptoAmount')
        tv.column('KryptoAmount', anchor='center', width=50)
        tv.heading('KryptoAveragePaid', text='KryptoAveragePaid')
        tv.column('KryptoAveragePaid', anchor='center', width=40)
        tv.heading('KryptoPersofinv', text='% of Investments')
        tv.column('KryptoPersofinv', anchor='center', width=40)
        tv.heading('MaxAllowedPersofInv', text='MaxAllowedPersofInv')
        tv.column('MaxAllowedPersofInv', anchor='center', width=80)
        tv.heading('KryptoPaidValue', text='KryptoPaidValue')
        tv.column('KryptoPaidValue', anchor='center', width=80)
        tv.heading('KryptoTotalValue', text='KryptoTotalValue')
        tv.column('KryptoTotalValue', anchor='center', width=80)
        tv.heading('KryptoDiff', text='KryptoDiff')
        tv.column('KryptoDiff', anchor='center', width=80)
        tv.heading('KryptoTotalChange', text='KryptoTotalChange %')
        tv.column('KryptoTotalChange', anchor='center', width=80)
        tv.grid(sticky=(N, S, W, E))
        self.treeview = tv

    def LoadKryptoTable(self):
        for x in range(0, number_of_kryptos_int):
            self.treeview.insert('', 'end',
                                 text=krypto_name[x], values=(
                                 '%.2f' % krypto_current_pricefloat_list[x] + ' $', #2 OK
                                 '%.2f' % krypto_24h_price_list[x] + ' $', #3
                                 '%.2f' % krypto_daily_change_pers_list[x] + ' %', #3 OK
                                 '%.f' % krypto24hvolume_list[x] + ' $', #4 OK
                                 '%.2f' % krypto_amount_list[x] + ' ', #5 OK
                                 '%.2f' % krypto_gav_kurs_list[x] + ' ' + krypto_currency[x], #6 OK
                                 '%.2f' % krypto_percentage_list[x] + ' %', #7 NOK
                                 '%.2f' % krypto_max_pers_of_investments_list[x] + ' %', #10
                                 '%.f' % krypto_paid_list[x] + ' ' + currency, #11
                                 '%.f' % kryptovalue_list[x] + ' ' + currency, #12
                                 '%.f' % krypto_diff_list[x] + ' ' + currency, #13
                                 '%.2f' % krypto_total_pers_change_list[x] + ' %'
                                 ))

        ttk.Style().configure("Treeview", background="white",
                              foreground="black", fieldbackground="white")

class Stocktable(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUIStock()
        self.LoadStockTable()
        self.CreateUIKrypto()
        self.LoadKryptoTable()
        #self.LoadStockTableColor()
        self.CreateUISummary()
        self.LoadSummaryTable()
        self.CreateUIPersonalData()
        self.PersonalData()

        #Tkinter Grid Geometry Manager. Defines how to expand the widget if the resulting cell is larger than the widget itself.
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

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
        tv.column('recommendedbuy', anchor='center', width=50)
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

    def CreateUIKrypto(self):
        tv = Treeview(self)
        tv['columns'] = ('KryptoCurrentPrice', 'Krypto24hPrice', 'Krypto24hChange', 'Krypto24hVol', 'KryptoAmount', 'KryptoAveragePaid', 'KryptoPersofinv', 'MaxAllowedPersofInv',
                         'KryptoPaidValue', 'KryptoTotalValue', 'KryptoDiff', 'KryptoTotalChange')
        tv.heading("#0", text='Krypto', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('KryptoCurrentPrice', text='KryptoCurrentPrice')
        tv.column('KryptoCurrentPrice', anchor='center', width=50)
        tv.heading('Krypto24hPrice', text='Krypto24hPrice')
        tv.column('Krypto24hPrice', anchor='center', width=80)
        tv.heading('Krypto24hChange', text='Krypto24hChange')
        tv.column('Krypto24hChange', anchor='center', width=40)
        tv.heading('Krypto24hVol', text='Krypto24hVol')
        tv.column('Krypto24hVol', anchor='center', width=80)
        tv.heading('KryptoAmount', text='KryptoAmount')
        tv.column('KryptoAmount', anchor='center', width=50)
        tv.heading('KryptoAveragePaid', text='KryptoAveragePaid')
        tv.column('KryptoAveragePaid', anchor='center', width=40)
        tv.heading('KryptoPersofinv', text='% of Investments')
        tv.column('KryptoPersofinv', anchor='center', width=40)
        tv.heading('MaxAllowedPersofInv', text='MaxAllowedPersofInv')
        tv.column('MaxAllowedPersofInv', anchor='center', width=80)
        tv.heading('KryptoPaidValue', text='KryptoPaidValue')
        tv.column('KryptoPaidValue', anchor='center', width=80)
        tv.heading('KryptoTotalValue', text='KryptoTotalValue')
        tv.column('KryptoTotalValue', anchor='center', width=80)
        tv.heading('KryptoDiff', text='KryptoDiff')
        tv.column('KryptoDiff', anchor='center', width=80)
        tv.heading('KryptoTotalChange', text='KryptoTotalChange %')
        tv.column('KryptoTotalChange', anchor='center', width=80)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv


    def CreateUISummary(self):
        tv = Treeview(self)
        tv['columns'] = ('currprice', 'prevclose', 'daychangepers', 'buyunder', 'recommendedbuy', 'amount', 'gav', 'gav2',
                         'persofinvestment', 'maxpersofinvestment', 'paidvalue', 'totalvalue', 'difference', 'totalchange', 'selltarget')
        tv.heading("#0", text='Summary', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('currprice', text='')
        tv.column('currprice', anchor='center', width=150)
        tv.heading('prevclose', text='')
        tv.column('prevclose', anchor='center', width=150)
        tv.heading('daychangepers', text='Day Change Commodity')
        tv.column('daychangepers', anchor='center', width=120)
        tv.heading('buyunder', text='Day Change My Value')
        tv.column('buyunder', anchor='center', width=100)
        tv.heading('recommendedbuy', text='')
        tv.column('recommendedbuy', anchor='center', width=120)
        tv.heading('amount', text='')
        tv.column('amount', anchor='center', width=120)
        tv.heading('gav', text='')
        tv.column('gav', anchor='center', width=120)
        tv.heading('gav2', text='')
        tv.column('gav2', anchor='center', width=120)
        tv.heading('persofinvestment', text='% of Invs')
        tv.column('persofinvestment', anchor='center', width=100)
        tv.heading('maxpersofinvestment', text='Max % of Invs')
        tv.column('maxpersofinvestment', anchor='center', width=100)
        tv.heading('paidvalue', text='Paid Value')
        tv.column('paidvalue', anchor='center', width=100)
        tv.heading('totalvalue', text='Total Value')
        tv.column('totalvalue', anchor='center', width=100)
        tv.heading('difference', text='Difference')
        tv.column('difference', anchor='center', width=100)
        tv.heading('totalchange', text='Total Change %')
        tv.column('totalchange', anchor='center', width=100)
        tv.heading('selltarget', text='')
        tv.column('selltarget', anchor='center', width=100)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadStockTable(self):
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
                                 stock_amount_list[x],
                                 '%.2f' % stock_gav_kurs_list[x] + ' ' + stock_currency[x],
                                 '%.2f' % stock_percentage_list[x] +
                                 ' %', '%.2f' % stock_max_pers_of_investments_list[x] + ' %',
                                 '%.2f' % stock_paid_list[x] + ' ' + currency,
                                 '%.2f' % stockvalue_list[x] + ' ' + currency,
                                 '%.2f' % stock_diff_list[x] + ' ' + currency,
                                 '%.2f' % stock_total_pers_change_list[x] + ' %',
                                 sales_target[x]))
        '''

        '''    
        ttk.Style().configure("Treeview", background="white",
                              foreground="black", fieldbackground="white")

    def LoadKryptoTable(self):
        for x in range(0, number_of_kryptos_int):
            self.treeview.insert('', 'end',
                                 text=krypto_name[x], values=(
                                 '%.2f' % krypto_current_pricefloat_list[x] + ' $', #2 OK
                                 '%.2f' % krypto_24h_price_list[x] + ' $', #3
                                 '%.2f' % krypto_daily_change_pers_list[x] + ' %', #3 OK
                                 '%.f' % krypto24hvolume_list[x] + ' $', #4 OK
                                 '%.2f' % krypto_amount_list[x] + ' ', #5 OK
                                 '%.2f' % krypto_gav_kurs_list[x] + ' ' + krypto_currency[x], #6 OK
                                 '%.2f' % krypto_percentage_list[x] + ' %', #7 NOK
                                 '%.2f' % krypto_max_pers_of_investments_list[x] + ' %', #10
                                 '%.f' % krypto_paid_list[x] + ' ' + currency, #11
                                 '%.f' % kryptovalue_list[x] + ' ' + currency, #12
                                 '%.f' % krypto_diff_list[x] + ' ' + currency, #13
                                 '%.2f' % krypto_total_pers_change_list[x] + ' %'
                                 ))

        ttk.Style().configure("Treeview", background="white",
                              foreground="black", fieldbackground="white")
        

    def LoadStockTableColor(self):

        self.labels = []
        style = ttk.Style()
        style.configure("red.TLabel", background='red')
        style.configure("green.TLabel", background='green')
        style.configure("header.TLabel", font = '-weight bold')
        width = 7
        height = 7
        self.table.set(new_rand_df())
        #self.table = GridView(self)
        self.table.grid()

        '''    
        self.table = GridView(self)
        self.table.pack()
        self.table.set(new_rand_df())
        '''

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


    def LoadSummaryTable(self):
        self.treeview.insert('', 'end', text='Stocks', values=('', '', '', '%.2f' % stocks_daily_portfolio_development +
                                                         ' %', '', '', '', '', '%.2f' % stockspercentage +
                                                         ' %', stock_total_max_pers_of_investments +
                                                         ' %',  '%.f' % total_stocks_paid_value + ' ' + currency,
                                                         '%.f' % sumofallstocks + ' ' + currency,
                                                         '%.f' % allstocksdifference + ' ' + currency,
                                                         '%.2f' % stocks_total_change + ' %', ''))
        self.treeview.insert('', 'end', text='Kryptos', values=('', '', '', '%.2f' % kryptos_daily_portfolio_development +
                                                         ' %', '', '', '', '', '%.2f' % kryptospercentage +
                                                         ' %', krypto_total_max_pers_of_investments +
                                                         ' %',  '%.f' % total_kryptos_paid_value + ' ' + currency,
                                                         '%.f' % sumofallkryptos + ' ' + currency,
                                                         '%.f' % allkryptosdifference + ' ' + currency,
                                                         '%.2f' % kryptos_total_change + ' %', ''))
        self.treeview.insert('', 'end', text='Cash', values=(
        '', '', '', '', '', '', '', '', '%.2f' % cashpercentage + ' %', '', '', '%.f' % cashfloat + ' ' + currency, '', ''))
        self.treeview.insert('', 'end', text='Money in Real Estate 1', values=(
        '', '', '', '', '', '', '', '', '%.2f' % cashinapartment1percentage + ' %', '', '', '%.f' % cash_in_apartment1 +
                                                        ' ' + currency, '', ''))
        self.treeview.insert('', 'end', text='Money in Real Estate 2', values=(
        '', '', '', '', '', '', '', '', '%.2f' % cashinapartment2percentage + ' %', '', '',
                        '%.f' % cash_in_apartment2_float + ' ' + currency, '', ''))
        self.treeview.insert('', 'end', text='Money in Real Estate 3', values=(
        '', '', '', '', '', '', '', '', '%.2f' % cashinapartment3percentage + ' %', '', '',
                        '%.f' % cash_in_apartment3_float + ' ' + currency, '', ''))
        self.treeview.insert('', 'end', text='Other investments', values=(
        '', '', '', '', '', '', '', '', '%.2f' % otherinvestmentspercentage + ' %', '', '',
                        '%.f' % other_investmentsfloat + ' ' + currency, '', ''))
        self.treeview.insert('', 'end', text='Money loaned', values=(
        '', '', '', '', '', '', '', '', '%.2f' % loangivenspercentage + ' %', '', '',
                        '%.f' % loan_given_float + ' ' + currency, '', ''))
        self.treeview.insert('', 'end', text='Gold', values=(
        '%.2f' % goldusd + ' USD/Onz', '%.2f' % goldsek + ' SEK/Onz', '%.2f' % goldusdchangepers + ' %', '', 'GDX: '
                        + '%.2f' % goldgdxusd + ' $', 'GDX Change: ' + '%.2f' % goldgdxperschange + ' %', 'GDXJ: '
                        + '%.2f' % goldgdxjusd + ' $', 'GDXJ Change: ' + '%.2f' % goldgdxjperschange
                        + ' %', '%.2f' % goldpercentage + ' %', '', '', '%.f' % gold + ' ' + currency, '', ''))
        self.treeview.insert('', 'end', text='Current Oil rate', values=(
        '%.2f' % oilusd + ' USD/Barrel', '%.2f' % oilsek + ' SEK/Barrel', '%.2f' % oilusdchangepers + ' %', '', '',
                        '', '', '', 'Total: %.2f' % totalpercentage + ' %', '', '', '%.f' % sumofinvestments  +
                        ' ' + currency, '', ''))


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
        self.treeview.insert('', 'end', text='Canadian/Swedish exchange rate', values=(
            '1 CAD = ' + '%f' % cadsekratefloat + ' ' + 'SEK', '1 SEK = ' + '%f' % sekcadratefloat + ' ' + 'CAD', '',
            '', '', '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='USD/SEK exchange rate', values=(
            '1 USD = ' + '%f' % usdsekratefloat + ' SEK', '1 SEK = ' + '%f' % sekusdratefloat + ' ' + 'USD', '', '', '',
            '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='Philippine Peso/SEK exchange rate', values=(
            '1 PHP = ' + '%f' % phpsekratefloat + ' SEK', '1 SEK = ' + '%f' % sekphpratefloat + ' ' + 'PHP', '', '', '',
            '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='USD/Euro exchange rate', values=(
            '1 USD = ' + '%f' % usdeurratefloat + ' €', '1 € = ' + '%f' % eurusdratefloat + ' ' + 'USD', '', '', '', '',
            '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='Canadian/Euro exchange rate', values=(
            '1 CAD = ' + '%f' % cadeurratefloat + ' €', '1 € = ' + '%f' % eurcadratefloat + ' ' + 'CAD', '', '', '', '',
            '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='Minimum buy', values=(
        '%.f' % minimumbuyfloat + ' ' + currency, 'Loan', debt + ' ' + currency, 'Monthly salary', '%.f' % monthly_salary  + ' ' + currency, '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='Cash in Account 1', values=(
        '%.f' % cash_account1_float + ' ' + currency, 'Debt Interest rate', debt_interest_rate + ' %', 'Annual salary', '%.f' % annual_salary  + ' ' + currency, '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='Cash in Account 2', values=(
        '%.f' % cash_account2_float + ' ' + currency, 'Required % banks require paid for apart', pers_bank_require_downpayment_for_loan + ' %', '', '', '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='Loan given', values=(
        '%.f' % loan_given_float + ' ' + currency, 'Debt Interest rate', debt_interest_rate + ' %', '', '', '', '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='Real Estate 3', values=(
        '%.f' % cash_in_apartment3_float + ' ' + currency, '', '', '', '', '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='All available Cash', values=(
        '%.f' % cashfloat + ' ' + currency, 'Max amount of cash you can get, apartment', '%.f' % max_loan_cash + ' ' + currency, '', '', '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='Gold', values=(
        '%.f' % gold + ' ' + currency, 'How much more loan possible', '%.f' % how_much_more_loan_possible + ' ' + currency, '', '', '', '', '', '', '', '', 'Last Updated', ''))
        self.treeview.insert('', 'end', text='Other Investments', values=(
        '%.f' % other_investmentsfloat + ' ' + currency, 'Estimated apartment value', current_est_value_apartment + ' ' + currency, '', '', '', '', '', '', '', '', time.ctime(), ''))
        self.treeview.insert('', 'end', text='Sum of all investments', values=(
        '%.f' % sumofinvestments + ' ' + currency, 'Cash in apartment', '%.f' % cash_in_apartment1 + ' ' + currency, '', '', '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='Sum of all investments', values=(
        '%.f' % sumofinvestments + ' ' + currency, 'Cash in apartment 2', '%.f' % cash_in_apartment2_float + ' ' + currency,
        '', '', '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='Net worth', values=(
        '%.f' % net_worth  + ' ' + currency, 'Monthly loan payment', '%.f' % monthly_loan_payments + ' ' + currency, 'Financial Goal', '%.f' % dollar_goal + ' $', '%.f' % sek_goal +
         ' ' + currency, 'Missing from financial goal', '%.f' % missing_from_goal + ' ' + currency , '', '', '', '', ''))


def piechart():
    labels = 'Gold', 'Cash', 'Stocks', 'Other Investments', 'Cash in apartment 2'
    sizes = [gold, cashfloat, sumofallstocks, other_investmentsfloat, cash_in_apartment2_float]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'orange']
    explode = (0, 0, 0.1, 0, 0)  # explode Stocks

    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%3.2f%%', shadow=True, startangle=90)
    plt.title("Investments")
    plt.axis('equal')
    plt.show()

def piechart_inc_apartment():
    labels = 'Gold', 'Cash', 'Stocks', 'Other Investments', 'Cash in Apartment', 'Cash in apartment 2'
    sizes = [gold, cashfloat, sumofallstocks, other_investmentsfloat, cash_in_apartment1, cash_in_apartment2_float]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'brown', 'orange']
    explode = (0, 0, 0, 0, 0.1, 0)  # explode Stocks

    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%3.2f%%', shadow=True, startangle=90)
    plt.title("Investments, including cash in apartment")
    plt.axis('equal')
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
        stocks_tk.amount_entry.insert(x, stock_amount_list[x])
        stocks_tk.amount_entry.grid(row=x+1, column=3)

        stocks_tk.gav_kurs_entry = tkinter.Entry(stocks_tk)
        stocks_tk.gav_kurs_entry.insert(x, stock_gav_kurs_list[x])
        stocks_tk.gav_kurs_entry.grid(row=x+1, column=4)

        stocks_tk.currency_entry = tkinter.Entry(stocks_tk)
        stocks_tk.currency_entry.insert(x, stock_currency[x])
        stocks_tk.currency_entry.grid(row=x+1, column=5)

        stocks_tk.max_pers_of_investments_entry = tkinter.Entry(stocks_tk)
        stocks_tk.max_pers_of_investments_entry.insert(x, stock_max_pers_of_investments_list[x])
        stocks_tk.max_pers_of_investments_entry.grid(row=x+1, column=6)

        stocks_tk.stock_web_page_entry = tkinter.Entry(stocks_tk)
        stocks_tk.stock_web_page_entry.insert(x, stock_web_page[x])
        stocks_tk.stock_web_page_entry.grid(row=x+1, column=7)

        stocks_tk.sales_target_entry = tkinter.Entry(stocks_tk)
        stocks_tk.sales_target_entry.insert(x, sales_target_list[x])
        stocks_tk.sales_target_entry.grid(row=x+1, column=8)

        stocks_tk.save_button = tkinter.Button(stocks_tk, text="Save", command=donothing)
        stocks_tk.save_button.grid(row=x+2, column=8, sticky=tkinter.W)


def personal_data():
    personal = Tk()
    personal.title("Personal Data")
    personal.grid_rowconfigure(0, weight=1)
    personal.grid_columnconfigure(0, weight=1)
    personal.config(background="lightblue")

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
    personal.max_pers_of_investments_entry.insert(10, stock_max_pers_of_investments)
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
class Menues(Frame):
    def __init__(self):
        #Frame.__init__(self)
        self.FileMenu()
        self.GraphMenu()



    def FileMenu(self):
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Personal Data", command=personal_data)
        filemenu.add_command(label="My Stocks", command=my_stocks)
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="Settings", menu=filemenu)

        self.config(menu=menubar)

    def GraphMenu(self):
        graphmenu = Menu(self, tearoff=0)
        graphmenu.add_command(label="Investments Chart - Pie Diagram", command=piechart)
        graphmenu.add_command(label="Investments Chart + cash in apartment - Pie Diagram",
                              command=piechart_inc_apartment)
        self.add_cascade(label="Graphs", menu=graphmenu)
'''



def main():

    #Creates StockPortfolio main window
    root = Tk()
    root.wm_title("StockPortfolio")
    Stocktable(root)

    #Creates KryptoPortfolio
    root2 = Tk()
    root2.wm_title("KryptoPortfolio")
    Kryptotable(root2)
    #StatusBar(root)
    #Menues(root)

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Personal Data", command=personal_data)
    filemenu.add_command(label="My Stocks", command=my_stocks)
    filemenu.add_command(label="Exit", command=quit)
    menubar.add_cascade(label="Settings", menu=filemenu)

    graphmenu = Menu(menubar, tearoff=0)
    graphmenu.add_command(label="Investments Chart - Pie Diagram", command=piechart)
    graphmenu.add_command(label="Investments Chart + cash in apartment - Pie Diagram", command=piechart_inc_apartment)
    menubar.add_cascade(label="Graphs", menu=graphmenu)
    root.config(menu=menubar)

    root.mainloop()
    root2.mainloop()

if __name__ == '__main__':
    main()

