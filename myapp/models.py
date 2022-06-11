from django.db import models
from django.db.models import JSONField
    
class Hostname(models.Model):
    hostname = models.CharField('hostname', max_length=50)
    
    def __str__(self):
        return self.hostname
    
class GetInterfaces(models.Model):
    hostname = models.ForeignKey(Hostname, on_delete=models.PROTECT)
    updated_at = models.DateTimeField(auto_now=True)
    data = JSONField(blank=False, null=True)
    
    def __str__(self):
        return f'{self.hostname}-GetInterfaces-{self.updated_at}'