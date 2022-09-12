from django.contrib import admin

from .models import Complaint, Flat, Owner


class FlatsInline(admin.TabularInline):
    model = Owner.flats_in_property.through
    raw_id_fields = ('owner', 'flat')


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    inlines = [FlatsInline]
    list_display = ('address', 'price', 'new_building',
                    'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)
    readonly_fields = ('created_at',)
    search_fields = ('town', 'address')


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'flat')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    exclude = ['flats_in_property']
    inlines = [FlatsInline]
    list_display = ('fullname', 'phonenumber', 'pure_phone')
    search_fields = ('fullname', 'pure_phone')
