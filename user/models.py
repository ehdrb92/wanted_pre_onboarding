from django.db import models

from job_posting.models import Post

class User(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'user'

class Company(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'company'

class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        db_table = 'resume'