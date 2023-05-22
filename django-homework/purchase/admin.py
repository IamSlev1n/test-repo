from django.contrib import admin
from purchase.models import Purchase


# Register your models here.
@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    empty_value_display = 'No data about date'
    list_display = ('user', 'book', 'date')
