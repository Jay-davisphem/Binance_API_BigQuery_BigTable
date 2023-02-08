import time
import requests
from google.cloud import bigquery 
# Binance API endpoint for getting ticker data
TICKER_URL = "https://api.binance.com/api/v3/ticker/24hr"

# Symbol of the coins to retrieve data for
SYMBOLS = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT"]

# Interval between data retrieval in seconds
INTERVAL = 30


def write_to_bigquery():

    client = bigquery.Client()
    table_ref='qwiklabs-gcp-03-d75a9de1cac9.binance_rt.binance_dt' #enter the table_id from the dataset :) Follow me


    while True:
        ls=[]
        for symbol in SYMBOLS:
            # Retrieve the ticker data from Binance
            url = TICKER_URL + "?symbol=" + symbol
            response = requests.get(url)
            ticker_data = response.json()
            empt_dict={}

            #Retrieve the values for the various data points
            empt_dict['crypto_name']=f"{symbol}_{int(time.time())}"
            empt_dict['open_price'] = ticker_data["openPrice"]
            empt_dict['close_price'] = ticker_data["lastPrice"]
            empt_dict['high_price'] = ticker_data["highPrice"]
            empt_dict['low_price'] = ticker_data["lowPrice"]
            empt_dict['volume'] = ticker_data["volume"]
            ls.append(empt_dict)
        #print(ls)
        client.insert_rows_json(table_ref,ls)
   
        time.sleep(INTERVAL)
if __name__ == '__main__':
    write_to_bigquery()
  