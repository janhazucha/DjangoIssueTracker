from django.forms import ModelForm
from .models import Issue

class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ('title', 'description', 'author', 'assignee', 'category', 'status')