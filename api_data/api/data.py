# https://github.com/ranaroussi/yfinance
from metric.main_metric import *
import yfinance as yf
import pandas as pd
import requests
from datetime import date

now = date.today()

class Api:
    def __init__():
        try:
            response = requests.get("https://google.com", timeout=5)
            return True
        except requests.ConnectionError:
            return False

    def get_hist_price(company, period_month):
        ticker = yf.Ticker(company)
        hist = ticker.history(period_month)
        hist_array = hist['Open'].array
        return hist_array
    
    def get_ia_info(company, period_month):
        ticker = yf.Ticker(company)
        hist = ticker.history(period_month)
        return hist

    def get_price_day(company):
        ticker = yf.Ticker(company)
        data_day = ticker.history("1d")
        hist_array = data_day['Open'].array
        days_data = hist_array[0]
        return days_data
    
    def news(company):
        ticker = yf.Ticker(company)
        news_data = ticker.news
        return news_data
    
    def opt(company):
        ticker = yf.Ticker(company)
        opt = ticker.options
        return opt
    
    def cap(comany):
        asset = yf.Ticker(comany)
        info = asset.info
        if 'marketCap' in info:
            market_cap = info['marketCap']
            return market_cap
        else:
            return 0
    def rsi(company):
        global now
        
        data = yf.download(company, start="2023-05-01", end=now, interval = "1d")
        reversed_df = data.iloc[::-1]
        rsi = Metric.rsi(reversed_df,14)
        return rsi
