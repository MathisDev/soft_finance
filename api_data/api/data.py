import yfinance as yf
import pandas as pd
import requests
from datetime import date

now = date.today()

class Metric:
    def percent(av ,nv):
        resul = 0
        resul = ((nv - av) / av) * 100
        return resul
    
    def sma(company,period_month):
        data_hist_price = Api.get_hist_price(company, period_month)
        total_data = 0
        month_data = 0
        old_data = 0
        count = 0
        average = 0
        len_data = len(data_hist_price)
        for data in data_hist_price:
            average = average + data
        av = average / len_data
        return av

    def volacity(company,period_month):
        data_hist_price = Api.get_hist_price(company, period_month)
        total_data = 0
        month_vol = 0
        old_data = 0
        count = 0
        per_cent = 0
        len_data = len(data_hist_price) - 1
    
        data_hist_price = data_hist_price[: - 1]
        for data in data_hist_price:
            if count == 0:
                old_data = data
            else:
                per_cent = Metric.percent(old_data,data)
                if (per_cent <= 0):
                    per_cent  = per_cent * -1
                total_data = total_data + per_cent
                old_data = data
            count += 1
        month_vol = total_data / (len_data - 1)
        return month_vol

    def rsi(data, window=14, adjust=False):
        delta = data['Close'].diff(1).dropna()
        loss = delta.copy()
        gains = delta.copy()

        gains[gains < 0] = 0
        loss[loss > 0] = 0

        gain_ewm = gains.ewm(com=window - 1, adjust=adjust).mean()
        loss_ewm = abs(loss.ewm(com=window - 1, adjust=adjust).mean())
        RS = gain_ewm / loss_ewm
        RSI = 100 - 100 / (1 + RS)
        return RSI



class Api:
    def __init__():
        try:
            requests.get("https://google.com", timeout=5)
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
