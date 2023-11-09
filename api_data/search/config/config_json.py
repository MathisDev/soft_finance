import json
from pprint import pprint
import inquirer

path_config_file  = 'search/config/monitoring.json'

class config:
    def init_json():
        global path_config_file
        dictionary = {
            "monitor": ["NVDA","BTC_USD","ETH_USD","AAPL"]
        }
        # Serializing json
        json_object = json.dumps(dictionary, indent=4)
        # Writing to sample.json
        with open(path_config_file, "w") as outfile:
            outfile.write(json_object)
            
    def add_new_list(company_list):
        dictionary = {
            "monitor":company_list 
        }
        
        json_object = json.dumps(dictionary, indent=4)
        with open(path_config_file, "w") as outfile:
            outfile.write(json_object)
        
    def add_company(new_company):
        global path_config_file
        company_list = []
        fd = open(path_config_file)
        data = json.load(fd)
        for el in data["monitor"]:
            company_list.append(el)
        company_list.append(new_company)
        fd.close()
        config.add_new_list(company_list)

    def extract_list():
        global path_config_file
        company_list = []
        fd = open(path_config_file)
        data = json.load(fd)
        for el in data["monitor"]:
            company_list.append(el)
        fd.close()
        return company_list
