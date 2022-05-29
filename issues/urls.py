from django.urls import path
from .views import get_issues, create_issue

urlpatterns = [
    path('', get_issues, name='issues'),
    path('create', create_issue, name='createissue')
]