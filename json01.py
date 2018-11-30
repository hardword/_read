#!/bin/python
# json parsing from https://dev.to/twilio/working-with-json-in-python-4hd1

#import json #to use default json module
#import simplejson as json #to use simplejson module which is well maintained
import ujson as json #to use ultra json which is good for large data processing and (de)serialization


with open('nvdcve-1.0-20181128.json', 'ro') as f:
	json_text = f.read()

# json to dict
nvdcve_dict = json.loads(json_text)
print nvdcve_dict['CVE_data_timestamp']

# dict to json
new_json_string = json.dumps(nvdcve_dict, indent=4)
print new_json_string[0:100]

"""
import requests

apod_url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
apod_dict = requests.get(apod_url).json()

print(apod_dict['explanation'])
"""

"""
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/apod', methods=['GET'])
def apod():
        url = 'https://apod.nasa.gov/apod/image/1810/Orionids_Hao_960.jpg'
        title = 'Orionids Meteors over Inner Mongolia'

        return jsonify(url=url, title=title)

if __name__ == '__main__':
        app.run()
"""