import csv
import sys
import os
import pip
import time
print(pip.pep425tags.get_supported())
from lxml import html
import requests
import pandas as pd
import matplotlib.pyplot as plt
import json
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
import io
to_unicode = str
import pprint

pprint.pprint(sys.path)

script_dir = os.path.dirname(__file__)
personal_data_path = "stockportfolio\src\data\personal_data.json"
personal_data_abs_file_path = os.path.join(script_dir, personal_data_path)

with open(personal_data_abs_file_path, "r") as read_file:
    personal_data = json.load(read_file)

#personal_data
name = personal_data['name']
debt = personal_data['debt']
debt_townhouse = personal_data['debt_townhouse']
debt_interest_rate = personal_data['debt_interest_rate']
cash_account1 = personal_data['cash_account1']
cash_account2 = personal_data['cash_account2']
loan_given = personal_data['loan_given']
apartment3_estimated_value = personal_data['apartment3_estimated_value']
apartment4_estimated_value = personal_data['apartment4_estimated_value']
other_investments = personal_data['other_investments']
goldonz = personal_data['goldonz']
minimumbuy = personal_data['minimumbuy']
currency =personal_data['currency']
stock_total_max_pers_of_investments=personal_data['stock_max_pers_of_investments']
number_of_stocks=personal_data['number_of_stocks']
debtfloat = float(debt)
debt_townhouse_float = float(debt_townhouse)
debt_interest_ratefloat = float(debt_interest_rate)
goldonzfloat = float(goldonz)
cash_account1_float = float(cash_account1)
cash_account2_float = float(cash_account2)
cashfloat = cash_account1_float + cash_account2_float
loan_given_float = float(loan_given)

minimumbuyfloat = float(minimumbuy)
other_investmentsfloat = float(other_investments)

number_of_stocks_int = int(number_of_stocks)

pers_bank_require_downpayment_for_loan = personal_data['pers_bank_require_downpayment_for_loan']
current_est_value_apartment = personal_data['current_est_value_apartment']
monthly_loan_payments = personal_data['monthly_loan_payments']
cash_in_apartment2_float = personal_data['cash_in_apartment2']
monthly_salary = personal_data['monthly_salary']
annual_salary = personal_data['annual_salary']
dollar_goal = personal_data['dollar_goal']
number_of_kryptos = personal_data['number_of_kryptos']
krypto_total_max_pers_of_investments = personal_data['krypto_total_max_pers_of_investments']
cash_total_max_pers_of_investments = personal_data['cash_total_max_pers_of_investments']
real_estate_1_total_max_pers_of_investments = personal_data['real_estate_total_1_max_pers_of_investments']
real_estate_2_total_max_pers_of_investments = personal_data['real_estate_total_2_max_pers_of_investments']
real_estate_3_total_max_pers_of_investments = personal_data['real_estate_total_3_max_pers_of_investments']
real_estate_4_total_max_pers_of_investments = personal_data['real_estate_total_3_max_pers_of_investments']
other_investments_total_max_pers_of_investments = personal_data['other_investments_total_max_pers_of_investments']
loan_given_total_max_pers_of_investments = personal_data['loan_given_total_max_pers_of_investments']
gold_total_max_pers_of_investments = personal_data['gold_total_max_pers_of_investments']
real_estate_1_paid_amount = personal_data['real_estate_1_paid_amount']
real_estate_2_paid_amount = personal_data['real_estate_2_paid_amount']
real_estate_3_paid_amount = personal_data['real_estate_3_paid_amount']
real_estate_4_paid_amount = personal_data['real_estate_4_paid_amount']
real_estate_1_paid_amount_float = float(real_estate_1_paid_amount)
real_estate_2_paid_amount_float = float(real_estate_2_paid_amount)
real_estate_3_paid_amount_float = float(real_estate_3_paid_amount)
real_estate_4_paid_amount_float = float(real_estate_4_paid_amount)

number_of_kryptos_int = int(number_of_kryptos)

#Kryptos_data.json

kryptos_data_path = "stockportfolio\src\data\kryptos_data.json"
kryptos_data_abs_file_path = os.path.join(script_dir, kryptos_data_path)
with open(kryptos_data_abs_file_path, "r") as read_file:
  kryptos_data = json.load(read_file)
  print(kryptos_data)
  krypto_name_list = []
  krypto_amount_list = []
  krypto_gav_kurs_list = []
  krypto_max_pers_of_investments_list = []
  krypto_currency_list = []
  krypto_web_page_list = []

  for x in range(0, number_of_kryptos_int):
    krypto_name = kryptos_data['Kryptos'][x]['Krypto']
    krypto_amount = kryptos_data['Kryptos'][x]['KryptoAmount']
    krypto_amount_float = float(krypto_amount)
    krypto_gav_kurs = kryptos_data['Kryptos'][x]['KryptoAveragePaid']
    krypto_max_pers_of_investments = kryptos_data['Kryptos'][x]['KryptoMaxAllowedPersofInv']
    krypto_currency = kryptos_data['Kryptos'][x]['Currency']
    krypto_web_page = kryptos_data['Kryptos'][x]['KryptoWebPage']

    print("krypto_name: ", krypto_name)
    krypto_name_list = krypto_name_list + [krypto_name]
    krypto_amount_list = krypto_amount_list + [krypto_amount_float]
    krypto_gav_kurs_list = krypto_gav_kurs_list + [krypto_gav_kurs]
    krypto_max_pers_of_investments_list = krypto_max_pers_of_investments_list + [krypto_max_pers_of_investments]
    krypto_currency_list = krypto_currency_list + [krypto_currency]
    krypto_web_page_list = krypto_web_page_list + [krypto_web_page]

print("krypto_name_list[0] : " , krypto_name_list[0])
print("krypto_name_list[1] : " , krypto_name_list[1])
print("krypto_amount_list[0] : " , krypto_amount_list[0])
print("krypto_amount_list[1] : " , krypto_amount_list[1])
print("krypto_gav_kurs_list[0] : " , krypto_gav_kurs_list[0])
print("krypto_gav_kurs_list[1] : " , krypto_gav_kurs_list[1])
print("krypto_max_pers_of_investments_list[0] : " , krypto_max_pers_of_investments_list[0])
print("krypto_max_pers_of_investments_list[1] : " , krypto_max_pers_of_investments_list[1])
print("krypto_currency_list[0] : " , krypto_currency_list[0])
print("krypto_currency_list[1] : " , krypto_currency_list[1])
print("krypto_web_page_list[0] : " , krypto_web_page_list[0])
print("krypto_web_page_list[1] : " , krypto_web_page_list[1])

#stocks_data.json
stocks_data_path = "stockportfolio\src\data\stocks_data.json"
stocks_data_abs_file_path = os.path.join(script_dir, stocks_data_path)
with open(stocks_data_abs_file_path, "r") as read_file:
  stocks_data = json.load(read_file)
  print(stocks_data)
  stock_name_list = []
  stock_buy_price_recommendations_list = []
  stock_low_price_list = []
  stock_high_price_list = []
  stock_amount_list = []
  stock_sales_target_list = []
  stock_max_pers_of_investments_list = []
  stock_gav_kurs_list = []
  stock_currency_list = []
  stock_web_page_list = []

  for x in range(0, number_of_stocks_int):
    stock_name=stocks_data['Stocks'][x]['Stock']
    stock_buy_price_recommendations = stocks_data['Stocks'][x]['BuyUnder']
    stock_low_price = stocks_data['Stocks'][x]['LowPrice']
    stock_high_price = stocks_data['Stocks'][x]['HighPrice']
    stock_amount = stocks_data['Stocks'][x]['Amount']
    stock_sales_target = stocks_data['Stocks'][x]['SalesTarget']
    stock_max_pers_of_investments = stocks_data['Stocks'][x]['MaxPersOfInvestments']
    stock_gav_kurs = stocks_data['Stocks'][x]['GavKurs']
    stock_currency = stocks_data['Stocks'][x]['Currency']
    stock_web_page = stocks_data['Stocks'][x]['StockWebPage']

    print("stock_name: ",stock_name)
    print("stock_buy_price_recommendations: ", stock_buy_price_recommendations)
    print("stock_low_price: ", stock_low_price)
    print("stock_high_price: ", stock_high_price)
    print("stock_amount: ", stock_amount)
    print("stock_sales_target: ", stock_sales_target)
    print("stock_max_pers_of_investments: ", stock_max_pers_of_investments)
    print("stock_gav_kurs: ", stock_gav_kurs)
    print("stock_currency ", stock_currency)
    print("stock_web_page: ", stock_web_page)
    stock_name_list = stock_name_list + [stock_name]
    stock_buy_price_recommendations_list = stock_buy_price_recommendations_list + [stock_buy_price_recommendations]
    stock_low_price_list = stock_low_price_list + [stock_low_price]
    stock_high_price_list = stock_high_price_list + [stock_high_price]
    stock_amount_list = stock_amount_list + [stock_amount]
    stock_sales_target_list = stock_sales_target_list + [stock_sales_target]
    stock_max_pers_of_investments_list = stock_max_pers_of_investments_list + [stock_max_pers_of_investments]
    stock_gav_kurs_list = stock_gav_kurs_list + [stock_gav_kurs]
    stock_currency_list = stock_currency_list + [stock_currency]
    stock_web_page_list = stock_web_page_list + [stock_web_page]

print("stock_name_list[0] : " ,stock_name_list[0])
print("stock_name_list[1] : " ,stock_name_list[1])
print("stock_buy_price_recommendations_list[0] : " ,stock_buy_price_recommendations_list[0])
print("stock_buy_price_recommendations_list[1] : " ,stock_buy_price_recommendations_list[1])
print("stock_low_price_list[0] : " ,stock_low_price_list[0])
print("stock_low_price_list[1] : " ,stock_low_price_list[1])
print("stock_high_price_list[0] : " ,stock_high_price_list[0])
print("stock_high_price_list[1] : " ,stock_high_price_list[1])
print("stock_amount_list[0] : " ,stock_amount_list[0])
print("stock_amount_list[1] : " ,stock_amount_list[1])
print("stock_sales_target_list[0] : " ,stock_sales_target_list[0])
print("stock_sales_target_list[1] : " ,stock_sales_target_list[1])
print("stock_max_pers_of_investments_list[0] : ",stock_max_pers_of_investments_list[0])
print("stock_max_pers_of_investments_list[1] : " ,stock_max_pers_of_investments_list[1])

########################
#Exchange rates
########################

def returnexchangerate(xratescurrencywebpage):
    page = requests.get(xratescurrencywebpage)
    print("xrate page: ", xratescurrencywebpage)
    tree = html.fromstring(page.content)
    rate = tree.xpath('//*[@id="content"]/div[1]/div/div[1]/div/div/span[2]/text()')
    ratestr = ''.join(rate)
    print("ratestr: ", ratestr)
    replacespace = ratestr.replace('\xa0', '')
    exchangeratefloat = float(replacespace.replace(',', '.'))
    print("exchangeratefloat: ", exchangeratefloat)
    return exchangeratefloat


def returngoldrate(xecurrencywebpage):
    page = requests.get(xecurrencywebpage)
    tree = html.fromstring(page.content)
    #rate = tree.xpath('//*[@id="ucc-container"]/span[2]/span[2]/text()')
    rate = tree.xpath('//*[@id="historicalRateTbl"]/tbody/tr[2]/td[4]/text()')
    ratestr = ''.join(rate)
    print("ratestr: ",ratestr)
    replacespace = ratestr.replace('\xa0', '')
    goldrate = replacespace.replace(',', '')
    print("goldrate: ", goldrate)
    goldratefloat = float(goldrate.replace('.', '.'))
    print("goldratefloat: ", goldratefloat)
    return goldratefloat


eursekratefloat = returnexchangerate('https://www.x-rates.com/calculator/?from=EUR&to=SEK&amount=1')
#eursekratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1&From=EUR&To=SEK')
cadsekratefloat = returnexchangerate('https://www.x-rates.com/calculator/?from=CAD&to=SEK&amount=1')
usdsekratefloat = returnexchangerate('https://www.x-rates.com/calculator/?from=USD&to=SEK&amount=1')
phpsekratefloat = returnexchangerate('https://www.x-rates.com/calculator/?from=PHP&to=SEK&amount=1')
cadeurratefloat = returnexchangerate('https://www.x-rates.com/calculator/?from=CAD&to=EUR&amount=1')
usdeurratefloat = returnexchangerate('https://www.x-rates.com/calculator/?from=USD&to=EUR&amount=1')

sekeurratefloat = returnexchangerate('https://www.x-rates.com/calculator/?from=SEK&to=EUR&amount=1')
sekcadratefloat = returnexchangerate('https://www.x-rates.com/calculator/?from=SEK&to=CAD&amount=1')
sekusdratefloat = returnexchangerate('https://www.x-rates.com/calculator/?from=SEK&to=USD&amount=1')
sekphpratefloat = returnexchangerate('https://www.x-rates.com/calculator/?from=SEK&to=PHP&amount=1')
eurcadratefloat = returnexchangerate('https://www.x-rates.com/calculator/?from=EUR&to=CAD&amount=1')
eurusdratefloat = returnexchangerate('https://www.x-rates.com/calculator/?from=EUR&to=USD&amount=1')
#xauusdratefloat = returngoldrate('https://www.xe.com/sv/currencyconverter/convert/?Amount=1&From=XAU&To=USD')

xauusdratefloat=1
#phpsekratefloat=1
#xauusdratefloat=1
#usdsekratefloat=1

cash_in_apartment3_float1 = float(apartment3_estimated_value)
cash_in_apartment3_float = cash_in_apartment3_float1 * phpsekratefloat
cash_in_apartment4_float1 = float(apartment4_estimated_value)
cash_in_apartment4_float = cash_in_apartment4_float1 * phpsekratefloat

def returngoldusdchangepers():
    goldpage = requests.get('https://bors-nliv.svd.se/index.php/ravaror')
    goldtree = html.fromstring(goldpage.content)
    #print(goldtree)
    goldrate = goldtree.xpath('//*[@id="72831"]/td[3]/span[1]/text()')
    #print(goldrate)
    goldratestr = ''.join(goldrate)
    #print(goldratestr)
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
    print('oilrate: ', oilrate)
    oilratestr = ''.join(oilrate)
    print('oilratestr: ', oilratestr)
    oilratefloat = float(oilratestr.replace(',', '.'))
    print('oilratefloat: ', oilratefloat)
    return oilratefloat

def returnoilusdchangepers():
    oilpage = requests.get('https://bors-nliv.svd.se/index.php/ravaror')
    #goldpage = requests.get('https://www.bloomberg.com/markets/commodities/futures/metals')
    oiltree = html.fromstring(oilpage.content)
    #print(goldtree)
    oilrate = oiltree.xpath('//*[@id="42051"]/td[3]/span[1]/text()')
    #print(oilrate)
    oilratestr = ''.join(oilrate)
    #print(oilratestr)
    replaceplus = oilratestr.replace('+', '')
    replaceminus = replaceplus.replace('−', '-')
    oilratechangepersfloat = float(replaceminus.replace(',', '.'))
    #print(oilratechangepersfloat)
    return oilratechangepersfloat
'''
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
    print('goldgdxperschangerate: ', goldgdxperschangerate)
    goldgdxperschangeratestr = ''.join(goldgdxperschangerate)
    print('goldgdxperschangeratestr: ', goldgdxperschangeratestr)
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
'''

def returnkryptoforumreaders(kryptoforumreaderswebpage):
    #kryptoforumreaderspage = requests.get('https://www.reddit.com/r/Metaverse_Blockchain/')
    print('kryptoforumreaderswebpage1: ', kryptoforumreaderswebpage)
    if kryptoforumreaderswebpage == 0:
        print('kryptoforumreaderswebpage1 if 1: ', kryptoforumreaderswebpage)
        #kryptoforumreadersfloat = ''
        kryptoforumreadersstr = ''
    #elif kryptoforumreaderswebpage != '0':
    else:
        kryptoforumreaderspage = requests.get(kryptoforumreaderswebpage)
        print('kryptoforumreaderswebpage2 if 2: ', kryptoforumreaderswebpage)
        kryptoforumreaderstree = html.fromstring(kryptoforumreaderspage.content)
        print('kryptoforumreaderstree: ', kryptoforumreaderstree)
        kryptoforumreadersrate = kryptoforumreaderstree.xpath('normalize-space(/html/body/div[3]/div[5]/div/span[2]/span[1]/text())')
        print('kryptoforumreadersrate 1: ', kryptoforumreadersrate)
        if kryptoforumreadersrate == '':
            kryptoforumreadersrate = kryptoforumreaderstree.xpath('normalize-space(/html/body/div[3]/div[4]/div/span[2]/span[1]/text())')
            print('kryptoforumreadersrate 2: ', kryptoforumreadersrate)
            if kryptoforumreadersrate == '':
                kryptoforumreadersrate = kryptoforumreaderstree.xpath('normalize-space(/html/body/div[3]/div[5]/div/span[2]/span[1]/text())')
                print('kryptoforumreadersrate 3: ', kryptoforumreadersrate)
                if kryptoforumreadersrate == '':
                    kryptoforumreadersrate = kryptoforumreaderstree.xpath(
                        'normalize-space(/html/body/div[3]/div[5]/div/span[2]/span[1]/text())')
                    print('kryptoforumreadersrate 4: ', kryptoforumreadersrate)
        print('kryptoforumreadersrate: ', kryptoforumreadersrate)
        kryptoforumreadersstr = ''.join(kryptoforumreadersrate)
        print('kryptoforumreadersstr: ', kryptoforumreadersstr)
        #kryptoforumreadersfloat = float(kryptoforumreadersstr.replace(',', ''))
        #print('kryptoforumreadersfloat: ', kryptoforumreadersfloat)
    return kryptoforumreadersstr

#kryptoforumreaders = returnkryptoforumreaders()

#print('kryptoforumreaders: ', kryptoforumreaders)

########################
#Stock prices
########################
#Stock current price, Bloomberg, stopped working
#def stockcurrentpricebloomberg(bloombergwebpage):
    #page = requests.get(bloombergwebpage)
    #tree = html.fromstring(page.content)
      #price = tree.xpath('//*[@id="content"]/div/div/div[1]/div/div[4]/div[2]/text()')
      #price = tree.xpath('//*[@id="root"]/div/div/section[2]/div[1]/div/section[1]/section[1]/section[2]/section/div[1]/span[1]/text()')
      #price = tree.xpath('//*[@id="root"]/div/div/section[2]/div[1]/div/section/section[1]/section[2]/section/div[1]/span[1]/text()')
      #price = tree.xpath('//*[@id="root"]/div/div/section[2]/div[1]/div/section[1]/section/section[2]/section/div/span[1]/text()')
    #price = tree.xpath('//*[@id="root"]/div[1]/div[1]/section[2]/div[1]/div[1]/section[1]/section[1]/section[2]/section[1]/div[1]/span[1]/text()')
      #price = tree.xpath('//*[@id="root"]/div/div/section[2]/div[1]/div/section[1]/section/section[2]/section/div[1]/span[1]/text()')
    #print("price: ", price)
    #pricestr = ''.join(price)
    #print("pricestr: ", pricestr)
    #stockcurrentpricebloombergfloat = float(pricestr)
    #print("stockcurrentpricebloombergfloat: ", stockcurrentpricebloombergfloat)
    #return stockcurrentpricebloombergfloat

#Stock current price Wall Street Journal
def stockcurrentprice(webpage):
    page = requests.get(webpage)
    tree = html.fromstring(page.content)
    price = tree.xpath('//*[@id="quote_val"]/text()')
    #price = tree.xpath('//div[contains(@id,"data-reactid")]//p//text()')
    print("stock price: ", price)
    pricestr = ''.join(price)
    print("stock pricestr: ", pricestr)
    stockcurrentpricefloat = float(pricestr)
    print("stockcurrentpricefloat: ", stockcurrentpricefloat)
    return stockcurrentpricefloat

stock_current_pricefloat_list = []
for x in range(0, number_of_stocks_int):
    stock_current_pricefloat_list = stock_current_pricefloat_list + [(stockcurrentprice(stock_web_page_list[x]))]

#Krypto current price
def kryptocurrentprice(kryptowebpage):
    print("kryptowebpage: ", kryptowebpage)
    page = requests.get(kryptowebpage)
    print("page: ", page)
    tree = html.fromstring(page.content)
    print("tree: ", tree)
    price = tree.xpath('//span[@id="quote_price"]/span[1]/text()')
    print("Price: ", price)
    pricestr = ''.join(price)
    print("Pricestr: ", pricestr)
    if pricestr == '?':
        pricefloat = 0
        return pricefloat
    else:
        pricefloat = float(pricestr.replace('$', ' '))
        print("pricefloat: ", pricefloat)
        return pricefloat

#krypto_current_pricefloat_list
krypto_current_pricefloat_list = []
for x in range(0, number_of_kryptos_int):
    krypto_current_pricefloat_list = krypto_current_pricefloat_list + [(kryptocurrentprice(krypto_web_page_list[x]))]
    #stock_current_pricefloat_list = stock_current_pricefloat_list + [(stockcurrentpricebloomberg(stock_web_page[x]))]

#Stock previous close price Bloomberg
#def previousstockclose(bloombergwebpage):
    #page = requests.get(bloombergwebpage)
    #tree = html.fromstring(page.content)
    #change = tree.xpath('//*[@id="root"]/div/div/section[2]/div[1]/div/section[1]/div/section/section[2]/div/text()')
    #changestr = ''.join(change)
    #previousstockclosefloat = float(changestr)
    #return previousstockclosefloat

#Stock previous close price Wall Street Journal
def previousstockclose(webpage):
    page = requests.get(webpage)
    tree = html.fromstring(page.content)
    change = tree.xpath('//*[@id="compare_divId"]/div[3]/ul[1]/li[2]/span[2]/text()')
    print('previousstockclose change', change)
    changestr = ''.join(change)
    previousstockclosefloat = float(changestr)
    return previousstockclosefloat


previous_stock_closefloat_list = []
for x in range(0, number_of_stocks_int):
    previous_stock_closefloat_list = previous_stock_closefloat_list + [(previousstockclose(stock_web_page_list[x]))]

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
    print("krypto24hvolume")
    print("kryptowebpage: ", kryptowebpage)
    page = requests.get(kryptowebpage)
    print("page: ", page)
    tree = html.fromstring(page.content)
    print("tree: ", tree)
    #krypto24hvolume = tree.xpath('normalize-space(/html/body/div[3]/div/div[1]/div[4]/div[1]/div[2]/div[2]/text())')
    krypto24hvolume = tree.xpath('normalize-space(/html/body/div[2]/div/div[1]/div[4]/div[2]/div[2]/div/span[1]/span[1]/text())')
    print("krypto24hvolume: ", krypto24hvolume)
    krypto24hvolumestr = ''.join(krypto24hvolume)
    print("Krypto24hvolumestr: ", krypto24hvolumestr)
    krypto24hvolumestr1 = krypto24hvolumestr.replace('$', ' ')
    print("krypto24hvolumestr1: ", krypto24hvolumestr1)
    if (krypto24hvolumestr1 == '?' or krypto24hvolumestr1 == ''):
        krypto24hvolumestr1 = '0'
        krypto24hvolumefloat = float(krypto24hvolumestr1)
    else:
        krypto24hvolumefloat = float(krypto24hvolumestr1.replace(',', ''))
        print("krypto24hvolumefloat: ", krypto24hvolumefloat)
    return krypto24hvolumefloat

def krypto24hchangepers(kryptowebpage):
    print("krypto24changepers")
    print("kryptowebpage: ", kryptowebpage)
    page = requests.get(kryptowebpage)
    print("page: ", page)
    tree = html.fromstring(page.content)
    print("tree: ", tree)
    #price = tree.xpath('/html/body/div[3]/div/div[1]/div[3]/div[2]/span[2]/text()')
    price = tree.xpath('/html/body/div[2]/div/div[1]/div[4]/div[1]/div[1]/span[2]/span/text()')
    print("krypto24Price: ", price)
    pricestr = ''.join(price)
    print("krypto24Pricestr: ", pricestr)
    pricestr1 = pricestr.replace('(', '')
    print("krypto24pricestr1: ", pricestr1)
    pricestr2 = pricestr1.replace(')', '')
    print("krypto24pricestr2: ", pricestr2)
    if pricestr2 == '':
        pricefloat = 0
        return pricefloat
    else:
        pricefloat = float(pricestr2.replace('%', ''))
        print("krypto24pricefloat: ", pricefloat)
        return pricefloat

krypto_daily_change_pers_list = []
for x in range(0, number_of_kryptos_int):
    krypto_daily_change_pers_list = krypto_daily_change_pers_list + [(krypto24hchangepers(krypto_web_page_list[x]))]

krypto24hvolume_list = []
for x in range(0, number_of_kryptos_int):
    krypto24hvolume_list = krypto24hvolume_list + [(krypto24hvolume(krypto_web_page_list[x]))]

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

goldusd = xauusdratefloat
goldsek = xauusdratefloat * usdsekratefloat
gold = goldsek * goldonzfloat


#goldgdxusd = returngoldusdgdx()
#goldgdxperschange = returngoldusdgdxperschange()
#goldgdxjusd = returngoldusdgdxj()
#goldgdxjperschange = returngoldusdgdxjperschange()

#This should be enabled!!! Stopped working all of the sudden
#goldusdchangepers = returngoldusdchangepers()

#This should be enabled
#oilusdchangepers = returnoilusdchangepers()

#Value of Oil
#oilusd = returnoilusd()
#oilsek = returnoilusd() * usdsekratefloat

#Financial goal in SEK
sek_goal = dollar_goal * usdsekratefloat

#Total Current Value of stock
def stockvalue(amount, pricefloat, ratefloat):
    return amount*pricefloat*ratefloat

#Total Current Value of Krypto
def kryptovalue(amount, pricefloat, ratefloat):
    return amount*pricefloat*ratefloat


stock_exchangerate_from_list = []
for x in range(0, number_of_stocks_int):
    stock_exchangerate_from_list = stock_exchangerate_from_list + [stock_currency_list[x]]

krypto_exchangerate_from_list = []
for x in range(0, number_of_kryptos_int):
    krypto_exchangerate_from_list = krypto_exchangerate_from_list + [krypto_currency_list[x]]


stock_exchangerate_list = []
for x in range(0, number_of_stocks_int):
    stock_exchangerate_list = stock_exchangerate_list + [returnexchangerate('https://www.x-rates.com/calculator/?from=' + stock_exchangerate_from_list[x] + '&to=' + currency + '&amount=1' + '')]

krypto_exchangerate_list = []
for x in range(0, number_of_kryptos_int):
    krypto_exchangerate_list = krypto_exchangerate_list + [returnexchangerate('https://www.x-rates.com/calculator/?from=' + krypto_exchangerate_from_list[x] + '&to=' + currency + '&amount=1' + '')]


stockvalue_list = []
for x in range(0, number_of_stocks_int):
    stockvalue_list = stockvalue_list + [stockvalue(stock_amount_list[x], stock_current_pricefloat_list[x], stock_exchangerate_list[x])]

kryptovalue_list = []
for x in range(0, number_of_kryptos_int):
    kryptovalue_list = kryptovalue_list + [kryptovalue(krypto_amount_list[x], krypto_current_pricefloat_list[x], krypto_exchangerate_list[x])]

# Daily % change in stock value

stock_daily_change_pers_list = []
for x in range(0, number_of_stocks_int):
    stock_daily_change_pers_list = stock_daily_change_pers_list + [laststockpricechange(previous_stock_closefloat_list[x], stock_current_pricefloat_list[x])]


stock_paid_list = []
for x in range(0, number_of_stocks_int):
    stock_paid_list = stock_paid_list + [stockvalue(stock_gav_kurs_list[x], stock_amount_list[x], stock_exchangerate_list[x])]


krypto_paid_list = []
for x in range(0, number_of_kryptos_int):
    krypto_paid_list = krypto_paid_list + [kryptovalue(krypto_gav_kurs_list[x], krypto_amount_list[x], krypto_exchangerate_list[x])]


#Difference in price, current value - paid value
def stockdifference(totalvalue, totalpaid):
    return totalvalue-totalpaid

#Difference in price, current value - paid value
def kryptodifference(totalvalue, totalpaid):
    return totalvalue-totalpaid

#Difference in price, current value - paid value
def realestatedifference(totalvalue, totalpaid):
    return totalvalue-totalpaid

stock_diff_list = []
for x in range(0, number_of_stocks_int):
    stock_diff_list = stock_diff_list + [stockdifference(stockvalue_list[x], stock_paid_list[x])]

krypto_diff_list = []
for x in range(0, number_of_kryptos_int):
    krypto_diff_list = krypto_diff_list + [kryptodifference(kryptovalue_list[x], krypto_paid_list[x])]

real_estate_1_difference = realestatedifference(float(current_est_value_apartment), real_estate_1_paid_amount_float)
real_estate_2_difference = realestatedifference(cash_in_apartment2_float, real_estate_2_paid_amount_float)
real_estate_3_difference = realestatedifference(cash_in_apartment3_float, real_estate_3_paid_amount_float)
real_estate_4_difference = realestatedifference(cash_in_apartment4_float, real_estate_4_paid_amount_float)

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

#Total sum of current value of all Real Estates
sumofallrealestate = float(current_est_value_apartment) + cash_in_apartment2_float + cash_in_apartment3_float + cash_in_apartment4_float

#Total sum of all investments
sumofinvestments = cashfloat + sumofallstocks + sumofallkryptos + sumofallrealestate + gold + other_investmentsfloat + loan_given_float

net_worth = sumofinvestments - debtfloat - debt_townhouse
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
if total_stocks_close_value != 0:
    stocks_daily_portfolio_development = 100 * (sumofallstocks - total_stocks_close_value) / total_stocks_close_value
else:
    stocks_daily_portfolio_development = 1

#Stock development today
if total_kryptos_24h_value != 0:
    kryptos_daily_portfolio_development = 100 * (sumofallkryptos - total_kryptos_24h_value) / total_kryptos_24h_value
else:
    kryptos_daily_portfolio_development = 1

#Commodity's Percentage of all investments
cashpercentage = investmentpercentage(cashfloat, sumofinvestments)
goldpercentage = investmentpercentage(gold, sumofinvestments)
stockspercentage = investmentpercentage(sumofallstocks, sumofinvestments)
kryptospercentage = investmentpercentage(sumofallkryptos, sumofinvestments)
cashinapartment1percentage = investmentpercentage(cash_in_apartment1, sumofinvestments)
cashinapartment2percentage = investmentpercentage(cash_in_apartment2_float, sumofinvestments)
cashinapartment3percentage = investmentpercentage(cash_in_apartment3_float, sumofinvestments)
cashinapartment4percentage = investmentpercentage(cash_in_apartment4_float, sumofinvestments)
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
if total_stocks_paid_value != 0:
    stocks_total_change = 100 * allstocksdifference / total_stocks_paid_value
else:
    stocks_total_change = 1

#Total % change, all kryptos
if total_kryptos_paid_value != 0:
    kryptos_total_change = 100 * allkryptosdifference / total_kryptos_paid_value
else:
    kryptos_total_change = 1

#Total % change Real Estates
real_esteate_1_total_change = 100 * real_estate_1_difference / real_estate_1_paid_amount_float
real_esteate_2_total_change = 100 * real_estate_2_difference / real_estate_2_paid_amount_float
real_esteate_3_total_change = 100 * real_estate_3_difference / real_estate_3_paid_amount_float
real_esteate_4_total_change = 100 * real_estate_4_difference / real_estate_4_paid_amount_float
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

stock_buy_recommendation_list = []
for x in range(0, number_of_stocks_int):
    stock_buy_recommendation_list = stock_buy_recommendation_list + [stock_buy(stock_max_pers_of_investments_list[x], stock_percentage_list[x],
                              stock_current_pricefloat_list[x], stock_buy_price_recommendations_list[x], cashfloat,
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


#Get deseired Currency exchanges
'''
eursekratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1&From=EUR&To=SEK')
cadsekratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1&From=CAD&To=SEK')
usdsekratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1&From=USD&To=SEK')
phpsekratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1&From=PHP&To=SEK')
cadeurratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1?From=CAD&To=EUR')
usdeurratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1?From=USD&To=EUR')

sekeurratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1&From=SEK&To=EUR')
sekcadratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1&From=SEK&To=CAD')
sekusdratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1&From=SEK&To=USD')
sekphpratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1&From=SEK&To=PHP')
eurcadratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1?From=EUR&To=CAD')
eurusdratefloat = returnexchangerate('http://www.xe.com/sv/currencyconverter/convert/?Amount=1&From=EUR&To=USD')
#xauusdratefloat = returnexchangerate('https://www.xe.com/sv/currencyconverter/convert/?Amount=1&From=XAU&To=USD')
xauusdratefloat=1
'''
#json
#Define data
def create_calculated_data_json():

  for x in range(0, number_of_stocks_int):
    stocks_calculated_data = {
    print(stock_name_list[x])
  }
  '''
  "Stocks": [
  {
  "stock[]": stock_name_list[x],
  "goldsek": goldsek,
  "gold": gold,
  }
  ]
    }
  '''

calculated_data = {
   "Currency Exchange Rates":[
      {
      'eursekratefloat': eursekratefloat,
      'sekeurratefloat': sekeurratefloat,
      'cadsekratefloat': cadsekratefloat,
      'sekcadratefloat': sekcadratefloat,
      'usdsekratefloat': usdsekratefloat,
      'sekusdratefloat': sekusdratefloat,
      'phpsekratefloat': phpsekratefloat,
      'sekphpratefloat': sekphpratefloat,
      'usdeurratefloat': usdeurratefloat,
      'eurusdratefloat': eurusdratefloat,
      'cadeurratefloat': cadeurratefloat,
      'eurcadratefloat': eurcadratefloat
    }
    ],
    "Golds": [
    {
      "goldusd": goldusd,
      "goldsek": goldsek,
      "gold": gold,
    }
    ],
    "Real Estates":  [
    {
      "real_esteate_1_total_change": real_esteate_1_total_change,
      "real_esteate_2_total_change": real_esteate_2_total_change,
      "real_esteate_3_total_change": real_esteate_3_total_change
    }
    ],
    "Stocks": [
    {
      "stocks_total_change": stocks_total_change
    }
    ],
    "Kryptos": [
    {
      "kryptos_total_change": kryptos_total_change
    }
    ]
    ,
  }


#Write Calculated data
calculated_data_path = "stockportfolio\src\data\calculated_data.json"
calculated_data_abs_file_path = os.path.join(script_dir, calculated_data_path)
with io.open(calculated_data_abs_file_path, 'w', encoding='utf8') as outfile:
    str_ = json.dumps(calculated_data,
                         indent=4, sort_keys=True,
                         separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))


    stock_data = {
    'Stock Data': {'foo': stocks_total_change,
                  'key': 'value',
                  'the answer': 42}}
    #with open('data\data.json', 'w') as outfile:
    #    json.dump(data, outfile)


    # Write JSON file
    with io.open(r'C:\Users\JannePC-Skylake\PycharmProjects\StockPortfolio\stockportfolio\src\data\stocks.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(stock_data,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))

#Compilation output
print('--------------------------------------------------------------------------------')
print('************ Welcome to Stock Portfolio,', name, '************')
print('--------------------------------------------------------------------------------')
print("Stock Portfolio development today", '%.2f' % stocks_daily_portfolio_development, '%')
print('--------------------------------------------------------------------------------')
print("Time updated: ", time.ctime())
print('--------------------------------------------------------------------------------')

#print('krypto_forum_list[0]: ', krypto_forum_list[0])
#print('krypto_forum_list[1]: ', krypto_forum_list[1])
#print('krypto_forum_list[2]: ', krypto_forum_list[2])
#print('krypto_forum_list[3]: ', krypto_forum_list[3])
#print('krypto_forum_list[4]: ', krypto_forum_list[4])
#print('krypto_forum_list[5]: ', krypto_forum_list[5])


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
        tv['columns'] = ('KryptoCurrentPrice', 'KryptoAmount', 'Krypto24hPrice', 'Krypto24hChange', 'Krypto24hVol',
                         'KryptoAveragePaid', 'KryptoPersofinv', 'MaxAllowedPersofInv',
                         'KryptoPaidValue', 'KryptoTotalValue', 'KryptoDiff', 'KryptoTotalChange', 'KryptoForum','KryptoForumOldValue')
        tv.heading("#0", text='Krypto', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('KryptoCurrentPrice', text='KryptoCurrentPrice')
        tv.column('KryptoCurrentPrice', anchor='center', width=50)
        tv.heading('KryptoAmount', text='KryptoAmount')
        tv.column('KryptoAmount', anchor='center', width=50)
        tv.heading('Krypto24hPrice', text='Krypto24hPrice')
        tv.column('Krypto24hPrice', anchor='center', width=80)
        tv.heading('Krypto24hChange', text='Krypto24hChange')
        tv.column('Krypto24hChange', anchor='center', width=40)
        tv.heading('Krypto24hVol', text='Krypto24hVol')
        tv.column('Krypto24hVol', anchor='center', width=80)
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
        tv.heading('KryptoForum', text='KryptoForum %')
        tv.column('KryptoForum', anchor='center', width=80)
        tv.heading('KryptoForumOldValue', text='KryptoForumOldValue %')
        tv.column('KryptoForumOldValue', anchor='center', width=80)
        tv.grid(sticky=(N, S, W, E))
        self.treeview = tv

    def LoadKryptoTable(self):
        for x in range(0, number_of_kryptos_int):
            self.treeview.insert('', 'end',
                                 text=krypto_name_list[x], values=(
                                 '%.2f' % krypto_current_pricefloat_list[x] + ' $',  #2 OK
                                 '%.4f' % krypto_amount_list[x] + ' ',  # 5 OK
                                 '%.2f' % krypto_24h_price_list[x] + ' $',  #3
                                 '%.2f' % krypto_daily_change_pers_list[x] + ' %',  #3 OK
                                 '%.f' % krypto24hvolume_list[x] + ' $',  #4 OK
                                 '%.2f' % krypto_gav_kurs_list[x] + ' $',  #6 OK
                                 '%.2f' % krypto_percentage_list[x] + ' %',  #7 NOK
                                 '%.2f' % krypto_max_pers_of_investments_list[x] + ' %',  #10
                                 '%.f' % krypto_paid_list[x] + ' ' + currency,  #11
                                 '%.f' % kryptovalue_list[x] + ' ' + currency,  #12
                                 '%.f' % krypto_diff_list[x] + ' ' + currency,  #13
                                 '%.2f' % krypto_total_pers_change_list[x] + ' %'
                                 #krypto_forum_list[x],
                                 #krypto_forum_old_value_list[x]
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
        tv['columns'] = ('currprice', 'amount', 'prevclose', 'daychangepers', 'buyunder', 'lowprice', 'highprice', 'recommendedbuy', 'gav', 'persofinvestment',
                         'maxpersofinvestment', 'paidvalue', 'totalvalue', 'difference', 'stocktotalchange', 'selltarget')
        tv.heading("#0", text='Stock', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('currprice', text='Current Price')
        tv.column('currprice', anchor='center', width=80)
        tv.heading('amount', text='Amount')
        tv.column('amount', anchor='center', width=50)
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
        tv.heading('stocktotalchange', text='Stock Total Change %')
        tv.column('stocktotalchange', anchor='center', width=80)
        tv.heading('selltarget', text='Sell Target')
        tv.column('selltarget', anchor='center', width=50)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv

    def CreateUIKrypto(self):
        tv = Treeview(self)
        tv['columns'] = ('KryptoCurrentPrice', 'KryptoAmount', 'Krypto24hPrice', 'Krypto24hChange', 'Krypto24hVol', 'KryptoAveragePaid', 'KryptoPersofinv', 'MaxAllowedPersofInv',
                         'KryptoPaidValue', 'KryptoTotalValue', 'KryptoDiff', 'KryptoTotalChange','KryptoForum','KryptoForumOldValue')
        tv.heading("#0", text='Krypto', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('KryptoCurrentPrice', text='KryptoCurrentPrice')
        tv.column('KryptoCurrentPrice', anchor='center', width=50)
        tv.heading('KryptoAmount', text='KryptoAmount')
        tv.column('KryptoAmount', anchor='center', width=50)
        tv.heading('Krypto24hPrice', text='Krypto24hPrice')
        tv.column('Krypto24hPrice', anchor='center', width=80)
        tv.heading('Krypto24hChange', text='Krypto24hChange')
        tv.column('Krypto24hChange', anchor='center', width=40)
        tv.heading('Krypto24hVol', text='Krypto24hVol')
        tv.column('Krypto24hVol', anchor='center', width=80)
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
        tv.heading('KryptoForum', text='KryptoForum %')
        tv.column('KryptoForum', anchor='center', width=80)
        tv.heading('KryptoForumOldValue', text='KryptoForumOldValue %')
        tv.column('KryptoForumOldValue', anchor='center', width=80)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv


    def CreateUISummary(self):
        tv = Treeview(self)
        tv['columns'] = ('currprice', 'amount', 'prevclose', 'daychangepers', 'buyunder', 'recommendedbuy', 'gav', 'gav2',
                         'persofinvestment', 'maxpersofinvestment', 'paidvalue', 'totalvalue', 'debt', 'difference', 'totalchange', 'selltarget')
        tv.heading("#0", text='Summary', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('currprice', text='')
        tv.column('currprice', anchor='center', width=150)
        tv.heading('amount', text='')
        tv.column('amount', anchor='center', width=120)
        tv.heading('prevclose', text='')
        tv.column('prevclose', anchor='center', width=150)
        tv.heading('daychangepers', text='Day Change Commodity')
        tv.column('daychangepers', anchor='center', width=120)
        tv.heading('buyunder', text='Day Change My Value')
        tv.column('buyunder', anchor='center', width=100)
        tv.heading('recommendedbuy', text='')
        tv.column('recommendedbuy', anchor='center', width=120)
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
        tv.heading('debt', text='Debt')
        tv.column('debt', anchor='center', width=100)
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
                                 text=stock_name_list[x], values=(
                                 '%.2f' % stock_current_pricefloat_list[x] + ' ' + stock_currency_list[x],
                                 stock_amount_list[x],
                                 '%.2f' % previous_stock_closefloat_list[x] + ' ' + stock_currency_list[x],
                                 '%.2f' % stock_daily_change_pers_list[x] +
                                 ' %', '%.2f' % stock_buy_price_recommendations_list[x] + ' ' + stock_currency_list[x],
                                 '%.2f' % stock_low_price_list[x] + ' ' + stock_currency_list[x],
                                 '%.2f' % stock_high_price_list[x] + ' ' + stock_currency_list[x],
                                 stock_buy_recommendation_list[x],
                                 '%.2f' % stock_gav_kurs_list[x] + ' ' + stock_currency_list[x],
                                 '%.2f' % stock_percentage_list[x] +
                                 ' %', '%.2f' % stock_max_pers_of_investments_list[x] + ' %',
                                 '%.2f' % stock_paid_list[x] + ' ' + currency,
                                 '%.2f' % stockvalue_list[x] + ' ' + currency,
                                 '%.2f' % stock_diff_list[x] + ' ' + currency,
                                 '%.2f' % stock_total_pers_change_list[x] + ' %',
                                 stock_sales_target_list[x]))
        '''

        '''    
        ttk.Style().configure("Treeview", background="white",
                              foreground="black", fieldbackground="white")

    def LoadKryptoTable(self):
        for x in range(0, number_of_kryptos_int):
            self.treeview.insert('', 'end',
                                 text=krypto_name_list[x], values=(
                                 '%.2f' % krypto_current_pricefloat_list[x] + ' $',  #2 OK
                                 '%.4f' % krypto_amount_list[x] + ' ',  # 5 OK
                                 '%.2f' % krypto_24h_price_list[x] + ' $',  #3
                                 '%.2f' % krypto_daily_change_pers_list[x] + ' %',  #3 OK
                                 '%.f' % krypto24hvolume_list[x] + ' $',  #4 OK
                                 '%.2f' % krypto_gav_kurs_list[x] + ' $',  #6 OK
                                 '%.2f' % krypto_percentage_list[x] + ' %',  #7 NOK
                                 '%.2f' % krypto_max_pers_of_investments_list[x] + ' %',  #10
                                 '%.f' % krypto_paid_list[x] + ' ' + currency,  #11
                                 '%.f' % kryptovalue_list[x] + ' ' + currency,  #12
                                 '%.f' % krypto_diff_list[x] + ' ' + currency,  #13
                                 '%.2f' % krypto_total_pers_change_list[x] + ' %'
                                 #krypto_forum_list[x],
                                 #krypto_forum_old_value_list[x]
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
                                                         ' %','%.f' % stock_total_max_pers_of_investments + ' %',
                                                         '%.f' % total_stocks_paid_value + ' ' + currency,
                                                         '%.f' % sumofallstocks + ' ' + currency, '',
                                                         '%.f' % allstocksdifference + ' ' + currency,
                                                         '%.2f' % stocks_total_change + ' %', ''))
        self.treeview.insert('', 'end', text='Kryptos', values=('', '', '', '%.2f' % kryptos_daily_portfolio_development +
                                                         ' %', '', '', '', '', '%.2f' % kryptospercentage +
                                                         ' %', '%.f' % krypto_total_max_pers_of_investments + ' %',
                                                         '%.f' % total_kryptos_paid_value + ' ' + currency,
                                                         '%.f' % sumofallkryptos + ' ' + currency, '',
                                                         '%.f' % allkryptosdifference + ' ' + currency,
                                                         '%.2f' % kryptos_total_change + ' %', ''))
        self.treeview.insert('', 'end', text='Cash', values=(
        '', '', '', '', '', '', '', '', '%.2f' % cashpercentage + ' %', '%.f' % cash_total_max_pers_of_investments +' %',
        '', '%.f' % cashfloat + ' ' + currency, '', ''))
        self.treeview.insert('', 'end', text='Slussplan', values=(
        '', '', '', '', '', '', '', '', '%.2f' % cashinapartment1percentage + ' %', '%.f' % real_estate_1_total_max_pers_of_investments + ' %',
        '%.f' % real_estate_1_paid_amount + ' ' + currency, '%.f' % float(current_est_value_apartment) + ' ' + currency,
                                                         '%.f' % debtfloat + ' ' + currency, '%.f' % real_estate_1_difference + ' ' + currency, '%.2f' % real_esteate_1_total_change + ' %'))
        self.treeview.insert('', 'end', text='Nils', values=(
        '', '', '', '', '', '', '', '', '%.2f' % cashinapartment2percentage + ' %', '%.f' % real_estate_2_total_max_pers_of_investments + ' %',
        '%.f' % real_estate_2_paid_amount + ' ' + currency,
                        '%.f' % cash_in_apartment2_float + ' ' + currency, '', '%.2f' % real_estate_2_difference + ' ' + currency, '%.2f' % real_esteate_2_total_change + ' %'))
        self.treeview.insert('', 'end', text='Montana Heights', values=(
        '', '', '', '', '', '', '', '', '%.2f' % cashinapartment3percentage + ' %', '%.f' %  real_estate_3_total_max_pers_of_investments + ' %',
                                '%.f' % real_estate_3_paid_amount_float + ' ' + currency,
                        '%.f' % cash_in_apartment3_float + ' ' + currency, '', '%.f' % real_estate_3_difference + ' ' + currency, '%.2f' % real_esteate_3_total_change + ' %'))
        self.treeview.insert('', 'end', text='Townhouse', values=(
        '', '', '', '', '', '', '', '', '%.2f' % cashinapartment4percentage + ' %', '%.f' %  real_estate_4_total_max_pers_of_investments + ' %',
                                '%.f' % real_estate_4_paid_amount_float + ' ' + currency,
                        '%.f' % cash_in_apartment4_float + ' ' + currency, '%.f' % debt_townhouse_float + ' ' + currency, '%.f' % real_estate_4_difference + ' ' + currency, '%.2f' % real_esteate_4_total_change + ' %'))
        self.treeview.insert('', 'end', text='Other investments', values=(
        '', '', '', '', '', '', '', '', '%.2f' % otherinvestmentspercentage + ' %', '%.f' % other_investments_total_max_pers_of_investments + ' %',
                                                         '%.f' % other_investmentsfloat + ' ' + currency,
                        '%.f' % other_investmentsfloat + ' ' + currency, '', ''))
        self.treeview.insert('', 'end', text='Money loaned', values=(
        '', '', '', '', '', '', '', '', '%.2f' % loangivenspercentage + ' %', '%.f' % loan_given_total_max_pers_of_investments + ' %','',
                        '%.f' % loan_given_float + ' ' + currency,'',''))
        self.treeview.insert('', 'end', text='Gold', values=(
        '%.2f' % goldusd + ' USD/Onz', '%.2f' % goldsek + ' SEK/Onz', '%.f' % goldonzfloat + ' Onz', '', '', '', '','', '%.2f' % goldpercentage + ' %', '%.f' % gold_total_max_pers_of_investments + ' %', '', '%.f' % gold + ' ' + currency, '' ))
                        #+ ' USD/Onz', '%.2f' % goldsek + ' SEK/Onz', '%.2f' % goldusdchangepers + ' %', '', 'GDX: '
                        #+ '%.2f' % goldgdxusd + ' $', 'GDX Change: ' + '%.2f' % goldgdxperschange + ' %', 'GDXJ: '
                        #+ '%.2f' % goldgdxjusd + ' $', 'GDXJ Change: ' + '%.2f' % goldgdxjperschange
                        #+ ' %', '', '%.f' % gold + ' ' + currency, '', ''))

        #self.treeview.insert('', 'end', text='Current Oil rate', values=(
        #'%.2f' % oilusd + ' USD/Barrel', '%.2f' % oilsek + ' SEK/Barrel', '%.2f' % oilusdchangepers + ' %', '', '',
                       # '', '', '', 'Total: %.2f' % totalpercentage + ' %', '', '', '%.f' % sumofinvestments  +
                       # ' ' + currency, '', ''))

    def CreateUIPersonalData(self):
        tv = Treeview(self)
        tv['columns'] = ('currprice', 'amount', 'prevclose', 'daychangepers', 'buyunder', 'recommendedbuy', 'gav',
                         'persofinvestment', 'maxpersofinvestment', 'paidvalue', 'totalvalue', 'difference', 'totalchange', 'selltarget')
        tv.heading("#0", text='Personal data', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('currprice', text='')
        tv.column('currprice', anchor='center', width=130)
        tv.heading('amount', text='')
        tv.column('amount', anchor='center', width=130)
        tv.heading('prevclose', text='')
        tv.column('prevclose', anchor='center', width=230)
        tv.heading('daychangepers', text='')
        tv.column('daychangepers', anchor='center', width=100)
        tv.heading('buyunder', text='')
        tv.column('buyunder', anchor='center', width=100)
        tv.heading('recommendedbuy', text='')
        tv.column('recommendedbuy', anchor='center', width=100)
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
        self.treeview.insert('', 'end', text='Euro/Swedish exchange rate', values=(
            '1 EUR = ' + '%f' % eursekratefloat + ' ' + 'SEK', '1 SEK = ' + '%f' % sekeurratefloat + ' ' + 'EUR', '',
            '', '', '', '', '', '', '', '', '', ''))
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
        '%.f' % minimumbuyfloat + ' ' + currency, 'Monthly salary', '%.f' % monthly_salary  + ' ' + currency, '', '', '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='Cash in Account 1', values=(
        '%.f' % cash_account1_float + ' ' + currency, 'Debt Interest rate', '%.f' % debt_interest_rate + ' %', 'Annual salary', '%.f' % annual_salary + ' ' + currency, '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='Cash in Account 2', values=(
        '%.f' % cash_account2_float + ' ' + currency, 'Required % banks require paid for apart', '%.f' % pers_bank_require_downpayment_for_loan + ' %', '', '', '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='Max amount of cash you can get, apartment', values=(
        '%.f' % max_loan_cash + ' ' + currency, '', '', '', '', '', '', '', '', '', '', '', '', ''))
        self.treeview.insert('', 'end', text='Net worth', values=(
        '%.f' % net_worth + ' ' + currency, 'Monthly loan payment', '%.f' % monthly_loan_payments + ' ' + currency, 'Financial Goal', '%.f' % dollar_goal + ' $', '%.f' % sek_goal +
         ' ' + currency, 'Missing from financial goal', '%.f' % missing_from_goal + ' ' + currency , 'Net worth + Debt',  '%.f' % sumofinvestments + ' ' + currency, 'Last Updated', time.ctime(), '', '', '' ))


def piechart():
    labels = 'Gold', 'Cash', 'Stocks', 'Other Investments', 'Cash in Real Estate 2', 'Cash in Real Estate 3'
    sizes = [gold, cashfloat, sumofallstocks, other_investmentsfloat, cash_in_apartment2_float, cash_in_apartment3_float]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'orange', 'blue']
    explode = (0, 0, 0.1, 0, 0, 0)  # explode Stocks

    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%3.2f%%', shadow=True, startangle=90)
    plt.title("Investments")
    plt.axis('equal')
    plt.show()

def piechart_inc_apartment():
    labels = 'Gold', 'Cash', 'Stocks', 'Other Investments', 'Cash in Real Estate 1', 'Cash in Real Estate 2', 'Cash in Real Estate 3'
    sizes = [gold, cashfloat, sumofallstocks, other_investmentsfloat, cash_in_apartment1, cash_in_apartment2_float, cash_in_apartment3_float]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'brown', 'orange', 'blue']
    explode = (0, 0, 0, 0, 0.1, 0, 0)  # explode Stocks

    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%3.2f%%', shadow=True, startangle=90)
    plt.title("Investments, including cash in Real Estate 1")
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
        stocks_tk.stock_name_entry.insert(x, stock_name_list[x])
        stocks_tk.stock_name_entry.grid(row=x+1, column=0)

        stocks_tk.buy_price_recommendations_entry = tkinter.Entry(stocks_tk)
        stocks_tk.buy_price_recommendations_entry.insert(x, stock_buy_price_recommendations_list[x])
        stocks_tk.buy_price_recommendations_entry.grid(row=x+1, column=1)

        stocks_tk.low_price_entry = tkinter.Entry(stocks_tk)
        stocks_tk.low_price_entry.insert(x, stock_low_price_list[x])
        stocks_tk.low_price_entry.grid(row=x+1, column=2)

        stocks_tk.high_price_entry = tkinter.Entry(stocks_tk)
        stocks_tk.high_price_entry.insert(x, stock_high_price_list[x])
        stocks_tk.high_price_entry.grid(row=x+1, column=2)

        stocks_tk.amount_entry = tkinter.Entry(stocks_tk)
        stocks_tk.amount_entry.insert(x, stock_amount_list[x])
        stocks_tk.amount_entry.grid(row=x+1, column=3)

        stocks_tk.gav_kurs_entry = tkinter.Entry(stocks_tk)
        stocks_tk.gav_kurs_entry.insert(x, stock_gav_kurs_list[x])
        stocks_tk.gav_kurs_entry.grid(row=x+1, column=4)

        stocks_tk.currency_entry = tkinter.Entry(stocks_tk)
        stocks_tk.currency_entry.insert(x, stock_currency_list[x])
        stocks_tk.currency_entry.grid(row=x+1, column=5)

        stocks_tk.max_pers_of_investments_entry = tkinter.Entry(stocks_tk)
        stocks_tk.max_pers_of_investments_entry.insert(x, stock_max_pers_of_investments_list[x])
        stocks_tk.max_pers_of_investments_entry.grid(row=x+1, column=6)

        stocks_tk.stock_web_page_entry = tkinter.Entry(stocks_tk)
        stocks_tk.stock_web_page_entry.insert(x, stock_web_page_list[x])
        stocks_tk.stock_web_page_entry.grid(row=x+1, column=7)

        stocks_tk.sales_target_entry = tkinter.Entry(stocks_tk)
        stocks_tk.sales_target_entry.insert(x, stock_sales_target_list[x])
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
        graphmenu.add_command(label="Investments Chart + cash in Real Estates - Pie Diagram",
                              command=piechart_inc_apartment)
        self.add_cascade(label="Graphs", menu=graphmenu)
'''



def main():

    #Creates StockPortfolio main window
    root = Tk()
    root.wm_title("StockPortfolio")
    Stocktable(root)

    #Creates KryptoPortfolio
    #root2 = Tk()
    #root2.wm_title("KryptoPortfolio")
    #Kryptotable(root2)
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
    graphmenu.add_command(label="Investments Chart + cash in Real Estates - Pie Diagram", command=piechart_inc_apartment)
    menubar.add_cascade(label="Graphs", menu=graphmenu)
    root.config(menu=menubar)
    create_calculated_data_json

    root.mainloop()
    #root2.mainloop()

if __name__ == '__main__':
    main()

