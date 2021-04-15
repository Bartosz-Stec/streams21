import requests
from requests.exceptions import HTTPError
import time
from datetime import datetime


URL_START='http://bitbay.net/API/Public/'
URL_END='USD/ticker.json'
INTERVAL=5

def crypto_get(data):
    try:
        response = requests.get( URL_START + data + URL_END)
        response.raise_for_status()

    except HTTPError as error_with_http:
        print(f'Błąd z adresem HTTP : {error_with_http}')

    else:
        originalData = response.json()
        return originalData["bid"], originalData["ask"]



while True:
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Lokalny czas =", dt_string)
    crypto_get('BTC')
    crypto_get('DASH')
    crypto_get('LTC')
    print('____________________________________________')
    time.sleep(INTERVAL)
