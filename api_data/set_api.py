from api.data import *
from search.scan import *
import os
import time
from datetime import date
import socket
from fastapi import FastAPI

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


# --- get metode --- #

print("INFO - API is running")
print("INFO - IP DE l'API :")
print(get_ip())

app = FastAPI()

@app.get("/rsi")
def rsi(comp: str):
    return Api.rsi(comp)

@app.get("/cap")
def cap(comp: str):
    return Api.cap(comp)

@app.get("/p_days")
def get_price_day(comp: str):
    return Api.get_price_day(comp)

@app.get("/news")
def news(comp: str):
    return Api.news(comp)

@app.get("/sma")
def sma(comp: str,period: str):
    return Metric.sma(comp,period)

@app.get("/vol")
def vol(comp: str,period: str):
    return Metric.volacity(comp,period)

# --- post metode --- #
