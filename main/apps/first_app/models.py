from __future__ import unicode_literals
from django.db import models

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validator(self,postData):
        errors = {}
        if len(postData['first_name']) < 3:
            errors['first_name'] = "First name should be more than 2 characters"
        if not re.match('^[a-z]*$', postData['first_name']):
            errors['charerror']="First name should be letters only"
        if len(postData['last_name']) < 3:
            errors['last_name'] = "Last name should be longer than 2 characters"
        if not re.match('^[a-z]*$', postData['last_name']):
            errors['charerror']="last name should be letters only"
        if len(postData['password']) < 5:
            errors['passwordlength'] = "password must be longer than 4"
        if postData['password'] != postData['confirm_password']:
            errors['passwordmatch'] = 'passwords do not match'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "invalid email"
        email_in_use = User.objects.filter(email = postData['email'])
        if email_in_use:
            errors['email_in_use'] = "email is already in use"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()