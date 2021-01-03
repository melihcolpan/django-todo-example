from datetime import datetime, timedelta
import pytz
from django.http import JsonResponse


def date_shift(days=30):
    return datetime.utcnow().replace(tzinfo=pytz.UTC) + timedelta(days=days)
