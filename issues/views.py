from django.shortcuts import render, redirect
from .models import Issue
from .forms import IssueForm

import json
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import IssueSerializer


def get_issues(request):
    issues_list = Issue.objects.all()
    return render(request, "issues.html", {'issues_list': issues_list})


def create_issue(request):
    form = IssueForm()

    if request.method == 'POST':
        print(request.POST)
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, "issueform.html", context)


@api_view(['GET'])
def rest_issues(request):
    issues_set = Issue.objects.all()
    serializer = IssueSerializer(issues_set, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_issue_by_id_rest(id):
    issue = Issue.objects.get(id=id)
    serializer = IssueSerializer(issue)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)
