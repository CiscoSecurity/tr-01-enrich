import requests
import json

tr_access_token = 'eyJhbGciO....bPito5n5Q' # Truncated example

url = 'https://visibility.amp.cisco.com/iroh/iroh-enrich/observe/observables'

headers = {'Authorization':'Bearer {}'.format(tr_access_token), 'Content-Type':'application/json', 'Accept':'application/json'}

observe_payload = [{'type': 'domain', 'value': 'cisco.com'}]

observe_payload = json.dumps(observe_payload)

response = requests.post(url, headers=headers, data=observe_payload)

print(response.json())