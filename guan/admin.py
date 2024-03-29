# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Address


class AddressAdmin(admin.ModelAdmin):
    readonly_fields = ('create_time', 'update_time', )
    list_display = ('id', 'name', 'description', 'region_id', 'longitude', 'latitude', 'img_obj_name', 'status', 'create_time', 'update_time',)
    search_fields = ('name',)


admin.site.register(Address, AddressAdmin)
