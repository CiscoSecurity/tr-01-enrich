import requests
import json

tr_access_token = 'eyJhbGciO....bPito5n5Q' # Truncated example

url = 'https://visibility.amp.cisco.com/iroh/iroh-enrich/refer/observables'

headers = {'Authorization':'Bearer {}'.format(tr_access_token), 'Content-Type':'application/json', 'Accept':'application/json'}

refer_payload = [{'type': 'domain', 'value': 'cisco.com'}]

refer_payload = json.dumps(refer_payload)

response = requests.post(url, headers=headers, data=refer_payload)

print(response.json())