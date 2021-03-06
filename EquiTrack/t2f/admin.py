from __future__ import unicode_literals

from django.contrib import admin

from t2f import models
from publics.admin import AdminListMixin


class TravelAdmin(admin.ModelAdmin):
    model = models.Travel
    list_filter = (
        'status',
        'traveler',
    )
    search_fields = (
        'reference_number',
    )
    list_display = (
        'reference_number',
        'traveler',
        'status',
        'start_date',
        'end_date',
    )
    readonly_fields = (
        'status',
    )


class TravelActivityAdmin(admin.ModelAdmin):
    model = models.TravelActivity
    list_filter = (
        'travel_type',
        'partner',
        'date',
        'travels'
    )
    search_fields = (
        'primary_traveler',
    )
    list_display = (
        'primary_traveler',
        'travel_type',
        'date'
    )


class ItineraryItemAdmin(admin.ModelAdmin):
    model = models.IteneraryItem
    list_filter = (
        'travel',
        'departure_date',
        'arrival_date',
        'origin',
        'destination'
    )
    search_fields = (
        'travel__reference_number',
    )
    list_display = (
        'travel',
        'departure_date',
        'arrival_date',
        'origin',
        'destination'
    )


class ActionPointAdmin(admin.ModelAdmin):
    model = models.ActionPoint
    list_filter = (
        'travel',
        'status',
    )
    search_fields = (
        'action_point_number',
        'travel__reference_number'
    )
    list_display = (
        'action_point_number',
        'travel',
        'description',
        'status',
        'completed_at',
    )


class ExpenseAdmin(AdminListMixin, admin.ModelAdmin):
    pass


class DeductionAdmin(AdminListMixin, admin.ModelAdmin):
    pass


class CostAssignmentAdmin(AdminListMixin, admin.ModelAdmin):
    pass


class ClearancesAdmin(AdminListMixin, admin.ModelAdmin):
    pass


class TravelAttachmentAdmin(AdminListMixin, admin.ModelAdmin):
    pass


class TravelPermissionAdmin(AdminListMixin, admin.ModelAdmin):
    pass


class InvoiceAdmin(AdminListMixin, admin.ModelAdmin):
    pass


class InvoiceItemAdmin(AdminListMixin, admin.ModelAdmin):
    pass



admin.site.register(models.TravelActivity, TravelActivityAdmin)
admin.site.register(models.Travel, TravelAdmin)
admin.site.register(models.IteneraryItem, ItineraryItemAdmin)
admin.site.register(models.ActionPoint, ActionPointAdmin)
admin.site.register(models.Expense, ExpenseAdmin)
admin.site.register(models.Deduction, DeductionAdmin)
admin.site.register(models.CostAssignment, CostAssignmentAdmin)
admin.site.register(models.Clearances, ClearancesAdmin)
admin.site.register(models.TravelAttachment, TravelAttachmentAdmin)
admin.site.register(models.Invoice, InvoiceAdmin)
admin.site.register(models.InvoiceItem, InvoiceItemAdmin)
