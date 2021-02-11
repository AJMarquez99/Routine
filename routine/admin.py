from django.contrib import admin

from .models import Refrigerator, Item
# Register your models here.

admin.site.register(Refrigerator)
admin.site.register(Item)
