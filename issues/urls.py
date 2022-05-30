from django.urls import path
from .views import get_issues, create_issue, edit_issue, get_issues_rest, get_issue_by_id_rest

urlpatterns = [
    path('', get_issues, name='get_issues'),
    path('create', create_issue, name='create_issue'),
    path('edit/<int:issue_id>', edit_issue, name='edit_issue'),

    #REST API
    path('get_issues_rest', get_issues_rest, name='get_issues_rest'),
    path('<int:id>', get_issue_by_id_rest, name='get_issue_by_id_rest'),

]