from django.contrib import admin
from .models import BillGroup, BillGroupMember, Bill

# Register your models here.

class BillGroupMemberInline(admin.TabularInline):
    model = BillGroupMember
    extra = 1

@admin.register(BillGroup)
class BillGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'currency')
    inlines = [BillGroupMemberInline]

    

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('payed_by', 'description', 'amount', 'payed_for_everyone')
