import requests, json

ip = "localhost"
urlAuth = "http://"+ip+"/jams/api/authentication/login"

loginInfo = json.dumps({
    "username": "",
    "password": ""
})

headers = {'Content-Type': 'application/json'}

auth = requests.request("POST", url=urlAuth, data=loginInfo, headers=headers)

accessToken = json.loads(auth.text)['access_token']

headers2 = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + accessToken
}

agentURL = "http://"+ip+"/jams/api/agent?name=TestNewAgent2"

agentDelete = requests.request("DELETE", url=agentURL, headers=headers2)

#Create dictionary object containing API response information
agentDelete_dict = agentDelete.json()

#Print response in formatted JSON 
formatResp = json.dumps(agentDelete_dict, indent=4)
print(formatResp)