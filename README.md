[![Gitter chat](https://img.shields.io/badge/gitter-join%20chat-brightgreen.svg)](https://gitter.im/CiscoSecurity/Threat-Response "Gitter chat")

### Threat Response Enrich APIs:

These scripts demonstrate the basics of interacting with the Threat Response Enrich APIs. 

### Before using you must update the following:
- tr_access_token

### Usage:
**Old way:**
```
python 01_deliberate_observables.py
```
**Or:**
- Update your config into config.conf file.
- Run main.py
```python3
python main.py
```
*This script was wrote in python 3.7.0*

### Example script output of old way: 
```
{'data': [{'module': 'AMP File Reputation', 'module-type': 'POKEDeliberateModule', 'data': {'verdicts': {'count': 0, 'docs': []}}}, {'module': 'Talos Intelligence', 'module-type': 'SenderBaseInvestigateModule', 'data': {'verdicts': {'count': 1, 'docs': [{'type': 'verdict', 'disposition': 1, 'observable': {'value': 'cisco.com', 'type': 'domain'}, 'valid_time': {'start_time': '2018-11-30T22:59:11.804Z', 'end_time': '2018-12-30T22:59:11.804Z'}}]}}}, {'module': 'Threat Grid', 'module-type': 'ThreatgridModule', 'data': {}}, {'module': 'Umbrella', 'module-type': 'OpenDNSInvestigateModule', 'data': {'verdicts': {'count': 1, 'docs': [{'type': 'verdict', 'disposition': 1, 'observable': {'value': 'cisco.com', 'type': 'domain'}, 'disposition_name': 'Clean', 'valid_time': {'start_time': '2018-11-30T22:59:11.507Z', 'end_time': '2018-12-30T22:59:11.507Z'}}]}}}, {'module': 'VirusTotal', 'module-type': 'VirusTotalInvestigateModule', 'data': {}}]}
```

### Example script output from main.py:
```
Read configuration successfull!
Get token access successfull!
[deliberate_observables] - {'data': [{'module': 'AMP File Reputation', 'module_instance_id': 'ddcf41a2-3ecb-43e8-b5b2-0e36ad2e16f3', 'module_type_id': '1898d0e8-45f7-550d-8ab5-915f064426dd', 'data': {'verdicts': {'count': 0, 'docs': []}}}, {'module': 'Talos Intelligence', 'module_instance_id': 'f14a7465-a77a-4e28-8b97-23706a56eab5', 'module_type_id': '2460c99b-2f01-523b-a65d-30a3c6603245', 'data': {'verdicts': {'count': 1, 'docs': [{'type': 'verdict', 'disposition': 5, 'observable': {'value': 'hpt.vn', 'type': 'domain'}, 'disposition_name': 'Unknown', 'valid_time': {'start_time': '2021-06-10T05:12:52.043Z', 'end_time': '2021-07-10T05:12:52.043Z'}}]}}}]}
[observe_observables] - {'data': [{'module': 'Talos Intelligence', 'module_instance_id': 'd83800c1-01be-4500-9399-e91b6bcc4cbe', 'module_type_id': '2460c99b-2f01-523b-a65d-30a3c6603245', 'data': {'verdicts': {'count': 1, 'docs': [{'type': 'verdict', 'disposition': 5, 'observable': {'value': 'hpt.vn', 'type': 'domain'}, 'judgement_id': 'transient:3d9199b8-c2f0-4472-b57d-993f43125ffd', 'disposition_name': 'Unknown', 'valid_time': {'start_time': '2021-06-10T05:12:53.874Z', 'end_time': '2021-07-10T05:12:53.874Z'}}]}, 'judgements': {'count': 1, 'docs': [{'valid_time': {'start_time': '2021-06-10T05:12:53.874Z', 'end_time': '2021-07-10T05:12:53.874Z'}, 'schema_version': '1.1.3', 'observable': {'value': 'hpt.vn', 'type': 'domain'}, 'type': 'judgement', 'source': 'Talos Intelligence', 'disposition': 5, 'reason': 'Neutral Talos Intelligence reputation score', 'source_uri': 'https://www.talosintelligence.com/reputation_center/lookup?search=hpt.vn', 'disposition_name': 'Unknown', 'priority': 90, 'id': 'transient:3d9199b8-c2f0-4472-b57d-993f43125ffd', 'severity': 'Low', 'tlp': 'white', 'confidence': 'High'}]}}}]}
[refer_observables] - {'data': [{'module': 'Talos Intelligence', 'module_instance_id': 'f14a7465-a77a-4e28-8b97-23706a56eab5', 'module_type_id': '2460c99b-2f01-523b-a65d-30a3c6603245', 'id': 'ref-talos-search-domain-hpt.vn', 'title': 'Search for this domain', 'description': 'Lookup this domain on Talos Intelligence', 'categories': ['Talos Intelligence', 'Search'], 'url': 'https://www.talosintelligence.com/reputation_center/lookup?search=hpt.vn'}]}
```