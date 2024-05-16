import json
import requests
import os

class userAPI:
    def __init__(self):
        self.url = 'http://awz66661.icu:8000'
        self.key = os.environ.get("APIAUTH")
        #self.key = 'api930080'

    def getusers(self):
        response = requests.get(self.url + '/users', params={"key": self.key})
        return json.loads(response.text)

    def gettest(self):
        response = requests.get(self.url + '/users/test', params={"key": self.key})
        return json.loads(response.text)

    def getdefault(self):
        response = requests.get(self.url + '/defaultemail', params={"key": self.key})
        return json.loads(response.text)
    
    def adduser(self, email, username):
        response = requests.post(self.url + "/users", params={"key": self.key, "email": email, "username": username})
        return json.loads(response.text)
    
    def deleteuser(self, email):
        response = requests.delete(self.url + "/users", params={"key": self.key, "email": email})
        return json.loads(response.text)

api = userAPI()
print(api.gettest())