import argparse
import json
import requests


#arugments parser
parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-n', type=str, help="Diagnostic Setting Name")
parser.add_argument('-s', type=str, help="Diagnostic Storage Account Setting ID ")
parser.add_argument('-k', type=str, help="Please use az account get-access-token --resource https://graph.microsoft.com and pass it.")


args = parser.parse_args()

bearer = args.k
bearer = bearer.replace('"', '')

# Setup Endpoints
headers = ({'Content-Type': 'application/json',
           'Authorization':  ('Bearer ' + bearer) })
body =  ({
    "id": "/providers/microsoft.aadiam/providers/microsoft.insights/diagnosticSettings/"+args.n,
    "name": args.n,
    "properties": {
        "logs": [{
            "category": "AuditLogs",
            "enabled": "true",
            "retentionPolicy": {
                "days": 3,
                "enabled": "true"
            }
        }, {
            "category": "SignInLogs",
            "enabled": "true",
            "retentionPolicy": {
                "days": 3,
                "enabled": "true"
            }
        }],
        "metrics": [],
        "storageAccountId": args.s
    }
})

json = json.dumps(body)

postaad = requests.put("https://management.azure.com/providers/microsoft.aadiam/diagnosticSettings/"+args.n+"?api-version=2017-04-01-preview", data=json, headers=headers)
print("Response:")
print(postaad)
