# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models


class GuanType(models.Model):
    name = models.CharField(max_length=50)
    created_time = models.DateTimeField(default=datetime.now)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "guan_type"

    def __unicode__(self):
        return self.name


class GuanGuan(models.Model):
    name = models.CharField(max_length=50)
    guan_type = models.ForeignKey(GuanType)
    guan_point = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    created_time = models.DateTimeField(default=datetime.now)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "guanguan"

    def __unicode__(self):
        return self.name


class GuanInfo(models.Model):
    question = models.CharField(max_length=200)
    guan = models.ForeignKey(GuanGuan)
    created_time = models.DateTimeField(default=datetime.now)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "guan_info"

    def __unicode__(self):
        return self.question


class AnswerInfo(models.Model):
    guan = models.ForeignKey(GuanGuan)
    guan_info = models.ForeignKey(GuanInfo)
    answer_key = models.CharField(max_length=200)
    answer_evaluation = models.CharField(max_length=50)
    created_time = models.DateTimeField(default=datetime.now)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "answer_info"

    def __unicode__(self):
        return self.answer_key


class OfflineMeeting(models.Model):
    guan = models.ForeignKey(GuanGuan)
    time = models.DateTimeField(default=datetime.now)
    address = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_time = models.DateTimeField(default=datetime.now)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "offline_meeting"

    def __unicode__(self):
        return self.address
