#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import pytz


def date_shift(days=30):
    return datetime.utcnow().replace(tzinfo=pytz.UTC) + timedelta(days=days)
