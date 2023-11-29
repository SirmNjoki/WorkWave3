from django.db import models
from django.contrib.auth.models import User
#
# # Create your models here.



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    is_employer = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=False)
class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    description = models.TextField()
#
class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField()
    resume = models.FileField(upload_to='resumes/')
