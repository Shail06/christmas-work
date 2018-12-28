from django.db import models

class Vendor(models.Model):
	vendor_name = models.CharField(max_length=200)
	hostname = models.CharField(max_length=50)
	logo = models.CharField(max_length=50)
	token = models.CharField(max_length=300)

	def __str__(self):
		return self.vendor_name

	def get_host_url(self):
		return self.hostname

	def get_logo_path(self):
		return self.logo

	def get_token(self):
		return self.token

	def get_endpoint(self, column_name):
		endpoints={
			"QUOTES": self.endpoint.quote_api,
			"EXCHANGE-RATE": self.endpoint.exchange_rate_api
		}
		return endpoints[column_name]

	def get_parameters(self, column_name):
		parameter_object={
			"QUOTES": self.quoteparameter,
			"EXCHANGE-RATE": ""
		}
		return parameter_object[column_name]



class Endpoint(models.Model):
	vendor_name = models.OneToOneField(Vendor, on_delete=models.CASCADE, primary_key=True,)
	quote_api = models.CharField(max_length=200)
	exchange_rate_api = models.CharField(max_length=200)

	def __str__(self):
		return "Endpoints-"+str(self.vendor_name)


class QuoteParameter(models.Model):
	vendor_name = models.OneToOneField(Vendor, on_delete=models.CASCADE, primary_key=True,)
	input_from = models.CharField(max_length=50)
	input_to = models.CharField(max_length=50)
	input_amount = models.CharField(max_length=50)
	remaining_attributes = models.CharField(max_length=400)
	response_amount = models.CharField(max_length=50)

	def __str__(self):
		return "Params-"+str(self.vendor_name)

class Currency(models.Model):
	currency_name = models.CharField(max_length=50)
	currency_code = models.CharField(max_length=3)

	def __str__(self):
		return self.currency_code +" - "+ self.currency_name

