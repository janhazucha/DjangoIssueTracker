from django.db import models
from django.contrib.auth.models import User

class Issue(models.Model):
    CATEGORY_CHOICES = (
        ('Bug', 'Bug'),
        ('Doc', 'Documentation'),
        ('Imp', 'Improvement')
    )

    STATUS_CHOICES = (
        ('ToDo', 'ToDo'),
        ('Proc', 'Processing'),
        ('Done', 'Done')
    )

    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    author = models.ForeignKey(User, related_name='issue_author', on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, related_name='issue_assignee', on_delete=models.CASCADE, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100, default='Bug')
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default='ToDo')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
