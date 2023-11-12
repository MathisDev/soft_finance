import requests
x = requests.get('http://127.0.0.1:8000/vol?comp=^FCHI&period=1mo')
print(x.text)
