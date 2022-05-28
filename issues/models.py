from django.db import models
from django.contrib.auth.models import User
from .utils import ChoiceEnum


class Issue(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    author = models.ForeignKey(User, related_name='issue_author', on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, related_name='issue_assignee', on_delete=models.CASCADE, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Status(ChoiceEnum):
        TODO = 'todo'
        PROCESSING = 'processing'
        DONE = 'done'

    class Category(ChoiceEnum):
        BUG = 'bug'
        DOCUMENTATION = 'documentation'
        IMPROVEMENT = 'improvement'
