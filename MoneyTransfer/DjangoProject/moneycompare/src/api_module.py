import requests
import json
import os
from ..models import Vendor, Endpoint

class APIClient:
    
    def __init__(self, website):
        self.vendor = Vendor.objects.get(vendor_name=website)
        self.endpoint = Endpoint.objects.get(vendor_name=self.vendor)
        self.hostname = self.vendor.get_host_url()
        self.token = self.vendor.get_token()
        self.set_default_headers()
    
    def set_endpoint(self, endpoint_column):
        self.endpoint = self.vendor.get_endpoint(endpoint_column)

    def set_default_headers(self):
        self.headers = {
            "Authorization": "Bearer " + self.token,
             'Content-Type': "application/json",
        }

    def get_parameter_object(self, endpoint_column):
        return self.vendor.get_parameters(endpoint_column)
        
    def set_request_type(self, request_type):
        self.request_type = request_type

    def send_request(self, payload, params):
        request_type = self.request_type
        url = self.hostname + self.endpoint
        headers = self.headers 
        response = requests.request(request_type, url, data=payload, headers=headers, params=params)
        return response.json()