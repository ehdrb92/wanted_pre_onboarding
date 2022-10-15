from django.db import models

from user.models import Company

class Post(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    country = models.CharField(max_length=10)
    region = models.CharField(max_length=10)
    position = models.CharField(max_length=20)
    compensation = models.PositiveIntegerField()
    skill = models.CharField(max_length=100)
    context = models.TextField()

    class Meta:
        db_table = 'post'