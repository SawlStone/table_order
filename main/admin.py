from django.contrib import admin

from .models import Table, TableOrder


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'seats')


@admin.register(TableOrder)
class TableOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'table', 'order_date', 'order_by_name', 'order_by_email')

