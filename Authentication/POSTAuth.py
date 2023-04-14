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

#Create dictionary object containing our authentication information
auth_dict = auth.json()

#Print response in formatted JSON 
formatResp = json.dumps(auth_dict, indent=4)
print(formatResp)