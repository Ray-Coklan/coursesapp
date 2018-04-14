from __future__ import unicode_literals
from django.db import models
from ..first_app.models import *

class CourseManager(models.Manager):
    def validator(self,postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = "Course name should be more than 5 characters"
        if len(postData['description']) < 15:
            errors['descriptioin'] = "Description should be more than 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = CourseManager()
    creator = models.ForeignKey(User, related_name="created_by")
    students = models.ManyToManyField(User, related_name="courses")
    