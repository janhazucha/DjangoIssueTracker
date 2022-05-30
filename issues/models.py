from django.db import models
from django.contrib.auth.models import User


class Issue(models.Model):
    CATEGORY_CHOICES = (
        ('Bug', 'Bug'),
        ('Documentation', 'Documentation'),
        ('Improvement', 'Improvement')
    )

    STATUS_CHOICES = (
        ('Todo', 'Todo'),
        ('Processing', 'Processing'),
        ('Done', 'Done')
    )

    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    author = models.ForeignKey(User, related_name='issue_author', on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, related_name='issue_assignee', on_delete=models.CASCADE, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100, default='Bug')
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default='Todo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_spent_time(self):
        delta = (self.updated_at - self.created_at).total_seconds()//60
        return delta
