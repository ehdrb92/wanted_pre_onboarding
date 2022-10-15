from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'user'

class Company(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'company'

class Resume(models.Model):
    user = models.ManyToManyField(User, through='UserResume')
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE)

    class Meta:
        db_table = 'resume'

class UserResume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_resume'