from django.contrib import admin

from apps.web.models import Customer, Payment

admin.site.register(Customer)
admin.site.register(Payment)
