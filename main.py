import requests
import json
import time

import logging
logfilename = "Mavex_{}.log".format(time.strftime("%d-%m-%y", time.gmtime()))
logging.basicConfig(filename=logfilename, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)


### GLOBAL 
fileconfig = "config.conf"
tr_access_token = ""
_config = dict()

### END GLOBAL DEFINE ###


def read_config():
	global _config
	with open(fileconfig, "r") as f:
		_config = json.loads(f.read().strip())

	if(_config is not None ):
		return True
	else:
		return False

def get_token_access():
	global tr_access_token
	headers = {'Content-Type':'application/x-www-form-urlencoded', 'Accept':'application/json'}
	payload = {'grant_type':'client_credentials'}
	response = requests.post(_config.get("token_url"), headers=headers, auth=(_config.get("client_id"), _config.get("client_password")), data=payload)
	tr_access_token = json.loads(response.content).get("access_token")

	return tr_access_token


def deliberate_observables(payload):
	headers = {'Authorization':'Bearer {}'.format(tr_access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
	deliberate_payload = json.dumps(payload)
	response = requests.post(_config.get("deliberate_url"), headers=headers, data=deliberate_payload)
	print("[deliberate_observables] - {}".format(response.json()))
	
def observe_observables(payload):
	headers = {'Authorization':'Bearer {}'.format(tr_access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
	observe_payload = json.dumps(payload)
	response = requests.post(_config.get("observe_url"), headers=headers, data=observe_payload)
	print("[observe_observables] - {}".format(response.json()))
	
def refer_observables(payload):
	headers = {'Authorization':'Bearer {}'.format(tr_access_token), 'Content-Type':'application/json', 'Accept':'application/json'}
	refer_payload = json.dumps(payload)
	response = requests.post(_config.get("refer_url"), headers=headers, data=refer_payload)
	print("[refer_observables] - {}".format(response.json()))
	


if __name__ == '__main__':
	if(read_config()):
		logging.info("[main] - Read configuration successfull!")
		print("Read configuration successfull!")
	else:
		logging.info("[main] - Read configuration unsuccessfull!")
		exit(1)

	if(get_token_access() is not None):
		logging.info("[main] - Get token access successfull!")
		print("Get token access successfull!")
	else:
		logging.info("[main] - Get token access unsuccessfull!")
		exit(1)


	deliberate_payload = [{'type': 'domain', 'value': 'hpt.vn'}]
	deliberate_observables(deliberate_payload)
	observe_observables(deliberate_payload)
	refer_observables(deliberate_payload)