# hack-day-twitter-scraper
Cloud Function to collect tweets related to IKEA using twitter API

# Architecture

![image](https://user-images.githubusercontent.com/30334967/204101587-428e3689-3b74-47a9-883a-3e8c5ab06468.png)

Here is a cloud function that can hit twitter API and collect the tweets related to IKEA and save in a big query database. 
To deploy just change the associated WIF and service account and run the workflow

# To-Do

1. Write Unit Test
2. Make use of Terraform to deploy the infra
