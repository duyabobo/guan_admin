# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models

from guan.qiniu_cdn import MyStorage


class Region(models.Model):
    province = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    area = models.CharField(max_length=128)
    status = models.IntegerField(default=1)
    create_time = models.DateTimeField(default=datetime.now)
    update_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "region"

    def __unicode__(self):
        return self.province + self.city + self.area


class Address(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=32)
    region = models.ForeignKey(Region)
    longitude = models.FloatField()
    latitude = models.FloatField()
    img = models.ImageField(storage=MyStorage())
    status = models.IntegerField(default=1)
    create_time = models.DateTimeField(default=datetime.now)
    update_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "address"

    def __unicode__(self):
        return self.name
