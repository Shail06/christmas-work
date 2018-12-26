from django.contrib import admin

# Register your models here.
from .models import Vendor, Endpoint, QuoteParameter, Currency

admin.site.register(Vendor)
admin.site.register(Endpoint)
admin.site.register(QuoteParameter)
admin.site.register(Currency)
