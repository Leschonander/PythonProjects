import requests
import json
import re
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
#geojson

req = requests.get('https://dc.jumpmobility.com/opendata/free_bike_status.json')

jsonData = json.loads(req.text)
# print(jsonData)
# print(jsonData['data']['bikes'])
# print(jsonData['data']['bikes'][0])


bikeId = pd.Series(jsonData['data']['bikes'][0]["bike_id"])
name = pd.Series(jsonData['data']['bikes'][0]["name"])
lon = pd.Series(jsonData['data']['bikes'][0]["lon"])
lat = pd.Series(jsonData['data']['bikes'][0]["lat"])
batLevel = pd.Series(jsonData['data']['bikes'][0]["jump_ebike_battery_level"])

for i in range(1, len((jsonData['data']['bikes']))):
    bikeId[i] = jsonData['data']['bikes'][i]["bike_id"]
    name[i] = jsonData['data']['bikes'][i]["name"]
    lon[i] = jsonData['data']['bikes'][i]["lon"]
    lat[i] = jsonData['data']['bikes'][i]["lat"]
    batLevel[i] = jsonData['data']['bikes'][i]["jump_ebike_battery_level"]

def p2f(x):
    '''convert string percent to float'''
    return float(x.strip('%'))/100

# Deal with percentage later...
# batLevel.replace('?','')
# astype('int32')
# print(batLevel)
'''
for row in batLevel:
    row.strip('%')
    print(row)
    int(row)
'''

bikes = pd.DataFrame({
    "Bike Id": bikeId,
    "Name": name,
    "Lat": lat,
    "Long": lon,
    "Battery Level": batLevel 
})
tables = bikes.to_html

# astype('int32')
chargeLevel = bikes["Battery Level"].str.strip('%')

chargeLevel = chargeLevel.astype('int32')
print(chargeLevel)

cords = pd.DataFrame({
    "Lat": lat,
    "Long": lon
})



cordDict = cords.to_dict('records')

# print(33 < chargeLevel, " " ,chargeLevel)
# print(66 < chargeLevel, " " ,chargeLevel)

charges = pd.DataFrame({
    "Charge Level": chargeLevel,
    "Below 33%":  chargeLevel.where(chargeLevel < 33) ,
    "Below 66%": chargeLevel.where(chargeLevel < 66),
    "Above 66%": chargeLevel.where(66 < chargeLevel)
})
# print(charges)
# print(charges.describe())
chargeDesc = charges.describe()

# print(charges["Below 33%"].count())
chargeCount = pd.DataFrame({
    "Low Charge": [charges["Below 33%"].count()],
    "Medium Charge": [charges["Below 66%"].count()],
    "High Charge": [charges["Above 66%"].count()],
    
})
# chargeCountTable = chargeCount.to_html

# chargeCount.plot.bar()
# plt.show()

# print(chargeCount)

# charges.plot.bar()
# plt.show()