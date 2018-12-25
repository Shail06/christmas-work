from django.contrib import admin

# Register your models here.
from .models import Vendor, Endpoint, QuoteParameter

admin.site.register(Vendor)
admin.site.register(Endpoint)
admin.site.register(QuoteParameter)
