import requests, json, os

ip = "localhost"
urlAuth = "http://"+ip+"/jams/api/authentication/login"

#Create your authentication payload
loginInfo = json.dumps({
    "username": "",
    "password": ""
})

headers = {
    'Content-Type': 'application/json'
}

#Authenticate and generate access token
auth = requests.request("POST", url=urlAuth, headers=headers, data=loginInfo)

#Store access token in a variable
accessToken = json.loads(auth.text)['access_token']

agentURL = "http://"+ip+"/jams/api/agent"

headers2 = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + accessToken
}

#Payload information needed to create new Agent definition
agentBody = json.dumps({
  "agentName": "PythonPOSTAgent",
  "agentTypeName": "Local",
  "agentType": "Local",
  "platformTypeName": "Windows",
  "agentPlatform": "Windows",
  "description": "Created by REST Call via Python",
  "jobCount": 0,
  "jobLimit": 999999,
  "licenseAllocated": "false",
  "online": "false",
  "properties": [
    {
      "propertyName": "Address",
      "categoryName": "Agent",
      "displayName": "Address",
      "typeName": "System.String",
      "typeNameSSO": "",
      "toolTip": "Enter the DNS Address to use when connecting to this Remote Host.",
      "description": "The DNS Address used to connect to this Remote Host.",
      "currentValue": "" 
    }
  ],
  "isExecutionAgent": "true",
  "acl": {
    "genericACL": [
      {
        "identifier": ".\Administrator",
        "inherited": "true",
        "flags": "ThisFolderOnly",
        "accessList": [
                        "Change",
                        "Inquire",
                        "Manage",
                        "Submit",
                        "Delete",
                        "Control"
        ]
      }
    ]
  }
})

#Create the new Agent definition
createAgent = requests.request("POST", data=agentBody, headers=headers2, url=agentURL)

#Create dictionary object containing API response information
createAgent_dict = createAgent.json()

#Print response in formatted JSON 
formatResp = json.dumps(createAgent_dict, indent=4)
print(formatResp)
