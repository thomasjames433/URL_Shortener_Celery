from django.db import models

# Create your models here.
from django.utils import timezone

class UrlModel(models.Model):
    longurl=models.URLField()
    shorturl=models.CharField(max_length=8)
    hitcount=models.IntegerField(default=0)
    hitcountperday=models.IntegerField(default=0)
    last_accessed=models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.longurl} -> {self.shorturl}"
    
    def update_datetime(self):
        self.last_accessed=timezone.now()
        self.save()