from metric.main_metric import *
from api.data import *
from menu.main_menu import *
from search.scan import *
import os
import time
from datetime import date

from fastapi import FastAPI

app = FastAPI()

# --- get metode --- #

@app.get("/rsi")
def rsi(comp: str):
    return Api.rsi(comp)

@app.get("/cap")
def cap(comp: str):
    return Api.cap(comp)

@app.get("/p_days")
def get_price_day(comp: str):
    return Api.days_data(comp)

@app.get("/news")
def news(comp: str):
    return Api.news(comp)

@app.get("/sma")
def sma(comp: str,period: str):
    return Metric.sma(comp,period)

@app.get("/vol")
def vol(comp: str,period: str):
    return Metric.volacity(comp,period)

@app.get("/ia_info")
def ia_info(comp: str,period: str):
    return Api.get_ia_info(company, period_month)
# --- post metode --- #
