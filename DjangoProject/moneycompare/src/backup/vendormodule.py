import json
from .apimodule import APIClient

class TransferWise:

    def __init__(self):
        self.twise_client = APIClient("transferwise")
        
    def get_exchange_rate_history(self, source, target, from_date, to_date, group):
        self.twise_client.set_endpoint("EXCHANGE-RATE")
        self.twise_client.set_request_type("GET")
        params = {"source": source, "target": target,
                       "from": from_date, "to": to_date, "group": group}
        payload = ""
        response = self.twise_client.send_request(payload, params)
        return response
    
    def get_exchange_rate(self, source, target):
        self.twise_client.set_endpoint("EXCHANGE-RATE")
        self.twise_client.set_request_type("GET")
        params = {"source": source, "target": target}
        payload = ""
        response = self.twise_client.send_request(payload, params)
        return response
        
    def get_temporary_quote(self, source, target, source_amount):
        self.twise_client.set_endpoint("QUOTES")
        self.twise_client.set_request_type("GET")
        params = {"source": source, 
                   "target": target, 
                   "sourceAmount": source_amount, 
                   "rateType": "FIXED",
                   "profile": ""}
                   
        payload = ""
        
        response = self.twise_client.send_request(payload, params)
        return response
        