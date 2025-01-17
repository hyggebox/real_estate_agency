from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Flat.owners.through
    extra = 3
    raw_id_fields = ('owner', 'flat',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']
    list_display = ('address', 'price', 'new_building', 'construction_year',
                    'town')
    list_editable = ['new_building']
    readonly_fields = ['created_at']
    list_filter = ['new_building', 'rooms_number', 'has_balcony', 'active']
    raw_id_fields = ('liked_by',)
    inlines = [OwnerInline]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'valid_phonenumber')
    raw_id_fields = ('flats',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
