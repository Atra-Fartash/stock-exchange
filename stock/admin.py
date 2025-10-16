from django.contrib import admin
from stock.models import Company, SaleRequest, BuyRequest


admin.site.register(Company)
admin.site.register(SaleRequest)
admin.site.register(BuyRequest)