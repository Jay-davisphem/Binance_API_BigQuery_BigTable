import time
import requests
from google.cloud import bigtable
from google.cloud.bigtable import column_family
from google.cloud.bigtable import row
from google.cloud import bigquery 
# Binance API endpoint for getting ticker data
TICKER_URL = "https://api.binance.com/api/v3/ticker/24hr"

# Symbol of the coins to retrieve data for
SYMBOLS = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "XRPUSDT"]

# Interval between data retrieval in seconds
INTERVAL = 30

def write_to_bigtable():

    client = bigtable.Client(project='project_id', admin=True)
    instance = client.instance('instance_id')
    table = instance.table('table_id')

    while True:
        for symbol in SYMBOLS:
            # Retrieve the ticker data from Binance
            url = TICKER_URL + "?symbol=" + symbol
            response = requests.get(url)
            ticker_data = response.json()

            open_price = ticker_data["openPrice"]
            close_price = ticker_data["lastPrice"]
            high_price = ticker_data["highPrice"]
            low_price = ticker_data["lowPrice"]
            volume = ticker_data["volume"]

            # Save the data in Bigtable
            column_family_id = "data"
            row_key = f"{symbol}_{int(time.time())}"
            row = table.row(row_key)
            row.set_cell(column_family_id, "open", open_price)
            row.set_cell(column_family_id, "close", close_price)
            row.set_cell(column_family_id, "high", high_price)
            row.set_cell(column_family_id, "low", low_price)
            row.set_cell(column_family_id, "volume", volume)
            row.commit()

    # Wait for the specified interval before retrieving the next set of data
        time.sleep(INTERVAL)


def write_to_bigquery():

    client = bigquery.Client()
    table_ref='table_id'


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
    write_to_bigtable()
    #write_to_bigquery()

