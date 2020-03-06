# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models


class GuanType(models.Model):
    name = models.CharField(max_length=50)
    created_time = models.DateTimeField(default=datetime.now())
    updated_time = models.DateTimeField(default=datetime.now())

    class Meta:
        db_table = "guan_type"
