from django.urls import path
from .views import get_issues, create_issue, rest_issues, get_issue_by_id_rest

urlpatterns = [
    path('', get_issues, name='issues'),
    path('create', create_issue, name='create_issue'),

    #REST API
    path('getIssues', rest_issues, name='get_issues'),
    path('<int:id>', get_issue_by_id_rest, name='get_issue_by_id_rest'),

]