# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models


class Address(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=32)
    region_id = models.IntegerField(default=0)
    longitude = models.FloatField()
    latitude = models.FloatField()
    created_time = models.DateTimeField(default=datetime.now)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "address"

    def __unicode__(self):
        return self.name
