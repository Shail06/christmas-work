import requests
import json
import os
from ..models import Vendor, Endpoint

class APIClient:
    
    def __init__(self, website):
        self.api_config = APIConfig(website)
        self.set_default_headers()
    
    def set_default_headers(self):
        self.headers = {
            "Authorization": "Bearer " + self.api_config.token,
             'Content-Type': "application/json",
        }
               
    def set_endpoint(self, endpoint):
        self.endpoint = self.api_config.read_config("endpoints")[endpoint]
        
    def set_request_type(self, request_type):
        self.request_type = request_type
                
    def send_request(self, payload, params):
        request_type = self.request_type
        url = self.api_config.hostname + self.endpoint
        headers = self.headers 
        response = requests.request(request_type, url, data=payload, headers=headers, params=params)
        return response.json()


class APIConfig:
    
    def __init__(self, website):
        self.website = website
        self.hostname = self.read_config("hostname")
        self.token = self.read_config("token")
    
    def read_config(self, attribute):
        with open(os.getcwd()+'/moneycompare/src/configuration.json') as f:
            config = json.load(f)
        return config[self.website][attribute]


