from django.db import models

"""Represents document model"""
class Document(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.name}--URL:{self.url}'