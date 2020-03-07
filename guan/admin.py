# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import GuanGuan
from models import GuanType
from models import GuanInfo


class GuanTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('created_time', 'updated_time')
    list_display = ('name', 'created_time', 'updated_time')
    search_fields = ('name',)


class GuanGuanAdmin(admin.ModelAdmin):
    readonly_fields = ('created_time', 'updated_time')
    list_display = ('name', 'guan_type', 'guan_point', 'status')
    search_fields = ('name',)


class GuanInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('created_time', 'updated_time')
    list_display = ('question', 'guan')
    search_fields = ('question',)


admin.site.register(GuanType, GuanTypeAdmin)
admin.site.register(GuanGuan, GuanGuanAdmin)
admin.site.register(GuanInfo, GuanInfoAdmin)
