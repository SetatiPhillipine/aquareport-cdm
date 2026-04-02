from django.contrib import admin
from .models import WaterFaultReport

@admin.register(WaterFaultReport)
class WaterFaultReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'fault_type', 'status', 'submitted_at')
    list_filter = ('status', 'fault_type')
    search_fields = ('name', 'location', 'description', 'phone')
    readonly_fields = ('submitted_at',)
    
    fieldsets = (
        ('Report Information', {
            'fields': ('user', 'name', 'gender', 'phone', 'location', 'fault_type', 'description')
        }),
        ('Admin Management', {
            'fields': ('status', 'admin_feedback'),
        }),
        ('Timestamps', {
            'fields': ('submitted_at',),
        }),
    )

    