from django.utils import timezone
from django.db import models

# Create your models here.

class Assets(models.Model):
    company_id  = models.CharField(max_length=100)
    asstes_name = models.CharField(max_length=100)
    request_by = models.PositiveIntegerField()
    request_accepted_by = models.PositiveIntegerField()
    request_reason = models.CharField(max_length=100)
    is_free = models.BooleanField(default=True)
    date_posted = models.DateField(default=timezone.now)
    image = models.ImageField(null=True,upload_to='images/')
    
        