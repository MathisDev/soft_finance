import requests

resp = requests.get('http://127.0.0.1:80/vol?comp=BTC-USD&period=1mo')
tab = resp.text
print(tab)


