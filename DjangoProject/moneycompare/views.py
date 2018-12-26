from django.shortcuts import render


from .src.vendor_service import VendorService

from .models import Vendor, Currency


def index(request):
	context = {}
	currency_list = Currency.objects.all()
	context['currency_list'] = currency_list
	return render(request, 'moneycompare/index.html', context)

def results(request):
	vendors_list = Vendor.objects.all()
	currency_list = Currency.objects.all()
	quote_collection = dict()
	context = {}
	source = request.POST['source-currency']
	target = request.POST['target-currency']
	sourceAmount = request.POST['source-amount']

	for vendor in vendors_list:
		vendor_object = VendorService(vendor.vendor_name)
		temporary_quote = ""
		quote_collection[vendor.vendor_name] = vendor_object.get_temporary_quote(source, target, sourceAmount)
	context['quote_collection']= quote_collection
	context['currency_list'] = currency_list
	return render(request, 'moneycompare/results.html', context)

	