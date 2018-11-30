[![Gitter chat](https://img.shields.io/badge/gitter-join%20chat-brightgreen.svg)](https://gitter.im/CiscoSecurity/Threat-Response "Gitter chat")

### Threat Response Enrich APIs:

These scripts demonstrate the basics of interacting with the Threat Response Enrich APIs. 

### Before using you must update the following:
- access_token

### Usage:
```
python  01_deliberate_observables.py
```

### Example script output: 
```
python  01_deliberate_observables.py
{'data': [{'module': 'AMP File Reputation', 'module-type': 'POKEDeliberateModule', 'data': {'verdicts': {'count': 0, 'docs': []}}}, {'module': 'Talos Intelligence', 'module-type': 'SenderBaseInvestigateModule', 'data': {'verdicts': {'count': 1, 'docs': [{'type': 'verdict', 'disposition': 1, 'observable': {'value': 'cisco.com', 'type': 'domain'}, 'valid_time': {'start_time': '2018-11-30T22:59:11.804Z', 'end_time': '2018-12-30T22:59:11.804Z'}}]}}}, {'module': 'Threat Grid', 'module-type': 'ThreatgridModule', 'data': {}}, {'module': 'Umbrella', 'module-type': 'OpenDNSInvestigateModule', 'data': {'verdicts': {'count': 1, 'docs': [{'type': 'verdict', 'disposition': 1, 'observable': {'value': 'cisco.com', 'type': 'domain'}, 'disposition_name': 'Clean', 'valid_time': {'start_time': '2018-11-30T22:59:11.507Z', 'end_time': '2018-12-30T22:59:11.507Z'}}]}}}, {'module': 'VirusTotal', 'module-type': 'VirusTotalInvestigateModule', 'data': {}}]}
```
