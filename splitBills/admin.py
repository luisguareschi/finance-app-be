from django.contrib import admin
from .models import BillGroup, BillGroupMember, Bill

# Register your models here.

class BillGroupMemberInline(admin.TabularInline):
    model = BillGroupMember
    extra = 1

class BillInline(admin.TabularInline):
    model = Bill
    extra = 1

@admin.register(BillGroup)
class BillGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'currency')
    inlines = [BillGroupMemberInline, BillInline]
