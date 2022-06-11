from django.db import models
from django.db.models import JSONField

class JsonData(models.Model):
    name = models.CharField('name', max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    jsondata = JSONField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.name}-{self.updated_at}'