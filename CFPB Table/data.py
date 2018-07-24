import requests
import json
import pandas as pd
import numpy as np 

req = requests.get('https://data.consumerfinance.gov/resource/jhzv-w97w.json')
jsonData = json.loads(req.text)

# print(jsonData) # Grab the entire dataset!

complaintAmount = len(jsonData)

company = pd.Series(jsonData[0]["company"])
product = pd.Series(jsonData[0]["product"])
issue = pd.Series(jsonData[0]["issue"])
dateR = pd.Series(jsonData[0]["date_received"])
response = pd.Series(jsonData[0]["company_response"])
state = pd.Series(jsonData[0]["zip_code"])


for i in range(1,1000):
    company[i] = jsonData[i]["company"]
    product[i] = jsonData[i]["product"]
    issue[i] = jsonData[i]["issue"]
    dateR[i] = jsonData[i]["date_received"]
    response[i] = jsonData[i]["company_response"]


df = pd.DataFrame({
    'Company': company,
    'Product': product,
    "Issue": issue,
    "Date Received": dateR,
    "Corporate Response": response

})
# print(df)
# print(df["Company"]) Grab it like that...

dfHTML = df.to_html #This saves the function to make the table...
tables = dfHTML

# response = pd.Series(jsonData[0]["company_public_response"])
# response[i] = jsonData[i]["company_public_response"]