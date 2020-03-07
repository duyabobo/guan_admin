# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import AnswerInfo
from models import GuanGuan
from models import GuanInfo
from models import GuanPoint
from models import GuanType
from models import OfflineMeeting


class GuanTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('created_time', 'updated_time')
    list_display = ('id', 'name', 'created_time', 'updated_time')
    search_fields = ('name',)


class GuanGuanAdmin(admin.ModelAdmin):
    readonly_fields = ('created_time', 'updated_time')
    list_display = ('id', 'name', 'guan_type', 'guan_point', 'status')
    search_fields = ('name',)


class GuanInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('created_time', 'updated_time')
    list_display = ('id', 'question', 'guan')
    search_fields = ('question',)


class AnswerInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('created_time', 'updated_time')
    list_display = ('id', 'guan', 'guan_info', 'answer_key', 'answer_evaluation')
    search_fields = ('answer_key',)


class OfflineMeetingAdmin(admin.ModelAdmin):
    readonly_fields = ('created_time', 'updated_time')
    list_display = ('id', 'guan', 'time', 'address', 'latitude', 'longitude')
    search_fields = ('answer_key',)


class GuanPointAdmin(admin.ModelAdmin):
    readonly_fields = ('created_time', 'updated_time')
    list_display = ('id', 'guan', 'guan_point', 'user_id')


admin.site.register(GuanType, GuanTypeAdmin)
admin.site.register(GuanGuan, GuanGuanAdmin)
admin.site.register(GuanInfo, GuanInfoAdmin)
admin.site.register(AnswerInfo, AnswerInfoAdmin)
admin.site.register(OfflineMeeting, OfflineMeetingAdmin)
admin.site.register(GuanPoint, GuanPointAdmin)
