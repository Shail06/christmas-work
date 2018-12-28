import json
from .api_module import APIClient

class VendorService:

    def __init__(self, vendor_name):
        self.api_client = APIClient(vendor_name)
        
    def get_exchange_rate_history(self, source, target, from_date, to_date, group):
        self.api_client.set_endpoint("EXCHANGE-RATE")
        self.api_client.set_request_type("GET")
        params = {"source": source, "target": target,
                       "from": from_date, "to": to_date, "group": group}
        payload = ""
        response = self.api_client.send_request(payload, params)
        return response
    
    def get_exchange_rate(self, source, target):
        self.api_client.set_endpoint("EXCHANGE-RATE")
        self.api_client.set_request_type("GET")
        params = {"source": source, "target": target}
        payload = ""
        response = self.api_client.send_request(payload, params)
        return response
        
    def get_temporary_quote(self, source, target, source_amount):
        self.api_client.set_endpoint("QUOTES")
        self.api_client.set_request_type("GET")
        quote_param = self.api_client.get_parameter_object("QUOTES")
        remaining_params = json.loads(quote_param.remaining_attributes)
        params = {
            quote_param.input_from: source,
            quote_param.input_to: target,
            quote_param.input_amount:source_amount,
            **remaining_params
        }
                   
        payload = ""    
        display_response = {}
        response = self.api_client.send_request(payload, params)
        display_response["converted_amount"] = response[quote_param.response_amount]
        display_response["target_currency"] = response[quote_param.response_target_currency]
        return display_response