from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
