# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import GuanType


class GuanTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('created_time', 'updated_time')
    list_display = ('name', 'created_time', 'updated_time')
    search_fields = ('name',)


admin.site.register(GuanType, GuanTypeAdmin)
