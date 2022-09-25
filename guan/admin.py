# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Address


class AddressAdmin(admin.ModelAdmin):
    readonly_fields = ('created_time', 'updated_time')
    list_display = ('id', 'name', 'created_time', 'updated_time')
    search_fields = ('name',)


admin.site.register(Address, AddressAdmin)
