from django.contrib import admin
from .models import CustomUser, Seller, Manager

admin.site.register(CustomUser)
admin.site.register(Seller)
admin.site.register(Manager)
