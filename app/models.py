from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Project(models.Model):
    name = models.CharField(max_length=255, null=True)
    client_name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    completed =  models.BooleanField(default=False)
    users = models.ManyToManyField(User, null=True,related_name="users")
    created_at = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    created_by = models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name="created_by")


    def __str__(self):
        return str(self.name)


class Client(models.Model):
    name = models.CharField(max_length=255,null=True)
    email_id = models.CharField(max_length=255, null=True)
    mobile_number = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    created_by = models.ForeignKey(User,null=True,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.name)





