from django.contrib import admin
from .models import Vehicle


@admin.display(description='Number Series')
def number_series(self, obj):
    return obj.number_series


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'series', 'create_timestamp')
    fields = ('id', 'number', 'maker', 'manufacturing_date', 'create_timestamp')
    list_display = ('number', 'maker', 'manufacturing_date', 'create_timestamp')
    list_filter = ('maker', 'series', )
    ordering = ('number', )


