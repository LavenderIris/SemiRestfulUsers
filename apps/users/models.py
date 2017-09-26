from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors["first_name"] = "First Name should be more than 1 character"
        if len(postData['last_name']) < 1:
            errors["last_name"] = "Last Name should be more than 1 character"
        if len(postData['email']) < 1:
            errors["email"] = "Email should be more than 1 character"
        return errors



# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = UserManager()
    # *************************