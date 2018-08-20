import argparse
import requests
import json

# Singer portion
import singer
import urllib.request

'''
def parse_arg():
    # Do we even, erm need it in this case? No key needed...
'''

def getJumpBikeAPI():
    schema = {'type': 'object',
    'properties':
    {
    'bike_id': {'type': 'string'},
    'name': {'type': 'string'},
    'lon': {'type': 'number'},
    'lat': {'type': 'number'},
    'is_reserved': {'type': 'integer'},
    'is_disabled': {'type': 'integer'},
    'jump_ebike_battery_level': {'type': 'string'}
    }}

    singer.write_schema('bikes',schema ,'bike_id') #StreamName, Schema, and indexer

    # Test so it doesn't run, forever???
    i = 0
    while i < 200:
        response = requests.get('https://dc.jumpmobility.com/opendata/free_bike_status.json')
        JSON = json.loads(response.text)
        body = JSON['data']['bikes']
        
        singer.write_records('bikes', body)
        i += 1
def main():
    '''
    To actually run the tap...
    '''
    # In theory a config would go here, but do we need it???
    getJumpBikeAPI()

if __name__ == '__main__':
    main()
'''
python jumpBikeTap.py | target-csv 
To actually run the program, which doesn't quite end yet???
'''