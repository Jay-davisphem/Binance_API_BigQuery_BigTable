# Binance_API_py:

Create a python script to retrieve data from binance api for few crypto coins and store 
them in google cloud bigtable and google cloud bigquery

## Stack Architecture:

<img src="/Architecture.png" width="300">

### Python Library Installation in Cloud Shell:

Pip install google-cloud-bigtable
Pip install google-cloud-bigquery
Pip install google-cloud-core

### Steps to do in Google Cloud Console:

1. Create a BigTable Instance and Table in Google Cloud BigTable
2. Create a Dataset and table in Googe Cloud BigQuery

### To View the output Data in Bigquery:

1. Go to BigQuery UI
2. Click the table name and view the data or write select * from `project_id.dataset.table_name`;

### To View the output Data in BigTable:

1. Go to Cloud Shell
2. echo project = `gcloud config get-value project` > ~/.cbtrc
3. echo instance = bigtable-instance >> ~/.cbtrc ### use your bigtable instance id instead of bigtable-instance
4. cbt read my-table  ### use your table-name instead of my-table. This command is used to view your data stored in bigtable

### Changes needs to be done in the Python Script:

1. Align the python code according to your project_id, dataset and table.
2. Then Run the code provide in the github.


