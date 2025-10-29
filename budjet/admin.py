from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'ttype', 'amount', 'category')
    list_filter = ('ttype', 'date', 'category')
    search_fields = ('category', 'description')
