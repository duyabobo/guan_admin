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
