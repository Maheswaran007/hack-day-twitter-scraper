import os
from google.cloud import bigquery
import pandas
from google.oauth2 import service_account
import pandas_gbq
from dotenv import load_dotenv
load_dotenv()

# CREDENTIALS GCP

bigqueryClient = bigquery.Client()


#UPDATE TABLE
def update_table(df4):
    
    tableRef = bigqueryClient.dataset("Ikea_tweets").table("Ikea_hackdays_tb")
    bigqueryJob = bigqueryClient.load_table_from_dataframe(df4, tableRef)
    print('Successfully Added into Bigquery')
    bigqueryJob.result()

