from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=20, null=False, blank=False)
    duration = models.PositiveSmallIntegerField()
    min_delegates = models.PositiveSmallIntegerField()
    max_delegates = models.PositiveSmallIntegerField()
    assessment = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    rrp = models.DecimalField(decimal_places=2, max_digits=8)
    ppp = models.DecimalField(decimal_places=2, max_digits=8)
    description = models.TextField()