import os
from google.cloud import bigquery
import pandas
from google.oauth2 import service_account
import pandas_gbq
from dotenv import load_dotenv
load_dotenv()
# Construct a BigQuery client object.


# CREDENTIALS GCP
#table_id = "bdpp-project-jency.IKEA_TWEETS.Ikea_Tweets_Tb"
gcpfilepath = os.getenv('GCP_CREDENTIALS')
print(gcpfilepath)
credentials = service_account.Credentials.from_service_account_file(gcpfilepath)
pandas_gbq.context.credentials = credentials
bigqueryClient = bigquery.Client(credentials=credentials)


#UPDATE TABLE
def update_dable(df4):
    print(df4.head())
    tableRef = bigqueryClient.dataset("Ikea_tweets").table("Tweet_hackdays_tb")
    bigqueryJob = bigqueryClient.load_table_from_dataframe(df4, tableRef)
    print('Successfully Added into Bigquery')
    bigqueryJob.result()

