import requests
import json
import os

ip = "localhost"
urlAuth = "http://"+ip+"/jams/api/authentication/login"

#Create your authentication payload
loginInfo = json.dumps({
    "username": "Administrator",
    "password": "HelpSystems1"
})

headers = {
  'Content-Type': 'application/json'
}

#Authenticate against the API and generate access token
response = requests.request("POST", url=urlAuth, data=loginInfo, headers=headers)

#Store token in a variable
accessToken = json.loads(response.text)['access_token']

#Specify Agent URL
agentURL = "http://"+ip+"/jams/api/agent"

headers2 = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + accessToken
}

#Call REST API, passing in URL and header information
getAgent = requests.request("GET", headers=headers2, url=agentURL)

#Create dictionary object containing API response information
getAgent_dict = getAgent.json()

#Print response in formatted JSON 
formatResp = json.dumps(getAgent_dict, indent=4)
print(formatResp)