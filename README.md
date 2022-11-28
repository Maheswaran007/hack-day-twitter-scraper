# hack-day-twitter-scraper
Cloud Function to collect tweets related to IKEA using twitter API

# Architecture


<img width="573" alt="Twitter5" src="https://user-images.githubusercontent.com/118686610/204370498-4583a071-0b4f-49f5-903c-11ac1da46b86.PNG">


Here is a cloud function that can hit twitter API and collect the tweets related to IKEA and save in a big query database. 
To deploy just change the associated WIF and service account and run the workflow

# To-Do

1. Write Unit Test
2. Make use of Terraform to deploy the infra
