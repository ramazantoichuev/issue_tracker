from django.contrib.auth.models import User
from django.db import models
from issue_tracker.models.base_model import BaseModel


class ProjectModel(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    users = models.ManyToManyField(User, blank=True, related_name='projects')

    def __str__(self):
        return self.name
