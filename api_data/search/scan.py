# import static
from search.config.config_json import *
from api.data import *
# import dynamique 
import numpy as np

def get_vol(array_company):
    dict_return = {} 
    for company in array_company:
        data_hist = Api.get_hist_price(company,"1mo")
        dict_return[company] = Metric.volacity(data_hist)
    return dict_return

def get_cap(array_company):
    dict_return = {}
    for company in array_company:
        dict_return[company] = Api.cap(company)
    return dict_return

def get_rsi(array_company):
    dict_return = {} 
    for company in array_company:
        dict_return[company] = Api.rsi(config.get_hist_price(company,"1m"))
    return dict_return

def data_scan(stat):
    dict_of_value = {}
    array_company = config.extract_list()
    if stat == "volacity":
        dict_of_value = tab_of_value = get_vol(array_company)
    elif stat == "CAP":
        dict_of_value = get_cap(array_company)
    elif stat == "RSI":
        dict_of_value = get_rsi(array_company)
    return (dict_of_value)

def sort_dict(dict,val):
    result_dict = {}
    for cle, valeur in dict.items():
        if valeur >= val:
            result_dict[cle] = valeur
    return result_dict

def main_search(stat,val):
    val =  float(val)
    dict_of_value = data_scan(stat) # un dic de tt les "company":"leux valeur x"
    sort_d = sort_dict(dict_of_value,val)
    print(sort_d)
    return sort_d