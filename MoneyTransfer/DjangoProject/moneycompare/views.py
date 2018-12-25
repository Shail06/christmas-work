from django.shortcuts import render


from .src.vendor_service import VendorService

from .models import Vendor


def index(request):
	context = {}
	vendors_list = Vendor.objects.all()
	quote_collection = dict()
	for vendor in vendors_list:
		vendor_object = VendorService(vendor.vendor_name)
		quote_collection[vendor.vendor_name] = vendor_object.get_temporary_quote("EUR", "CAD", 100)
	context['quote_collection']= quote_collection
	return render(request, 'moneycompare/index.html', context)