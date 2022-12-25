from django.utils import timezone
from django.db import models

# Create your models here.

class Assets(models.Model):
    company_id  = models.CharField(max_length=100)
    assets_name = models.CharField(max_length=100)
    request_by = models.PositiveIntegerField(null=True)
    request_accepted_by = models.PositiveIntegerField(null=True)
    request_reason = models.CharField(max_length=100)
    is_free = models.BooleanField(default=True)
    date_posted = models.DateField(default=timezone.now)
    image = models.CharField(max_length=100)

class AssetLogs(models.Model):
    activity = models.CharField(max_length=100)
    assets_id = models.PositiveIntegerField(null=True)
    accept_reason = models.CharField(max_length=100)
    date_of_activity = models.DateTimeField(default=timezone.now)

    
        