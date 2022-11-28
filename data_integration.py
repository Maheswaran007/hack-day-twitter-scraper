import os
from google.cloud import bigquery
import pandas
from google.oauth2 import service_account
from dotenv import load_dotenv
import config
load_dotenv()

# CREDENTIALS GCP

bigqueryClient = bigquery.Client()


#UPDATE TABLE
def update_table(df4):
    
    tableRef = bigqueryClient.dataset(config.dataset_id).table(config.table_id)
    bigqueryJob = bigqueryClient.load_table_from_dataframe(df4, tableRef)
    print('Successfully Added into Bigquery')
    bigqueryJob.result()
