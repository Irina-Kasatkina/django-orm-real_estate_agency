from django.contrib import admin

from .models import Complaint, Flat, Owner


class FlatAdmin(admin.ModelAdmin):
    list_display = ('address', 'owners_phonenumber', 'owner_pure_phone',
                    'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)
    readonly_fields = ('created_at',)
    search_fields = ('town', 'address')


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'flat')


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats_in_property',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
