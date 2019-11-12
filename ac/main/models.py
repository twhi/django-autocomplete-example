from django.db import models


# Create your models here.
class Test(models.Model):
    country = models.CharField(default='', max_length=100)
    name = models.CharField(default='', max_length=100)

    def __str__(self):
        return '{}'.format(self.country)
