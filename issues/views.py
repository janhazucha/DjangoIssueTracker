from django.shortcuts import render
from django.urls import reverse

from .models import Issue
from .forms import IssueForm

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponseRedirect
from .serializers import IssueSerializer


def get_issues(request):
    issues_list = Issue.objects.all().order_by('-created_at')
    deltas = []
    for i in issues_list:
        if i.status == 'Done':
            deltas.append(i.updated_at - i.created_at)
    max_spent_time = max(deltas)
    min_spent_time = min(deltas)
    return render(request, "issues.html", {'issues_list': issues_list, 'max_spent_time': max_spent_time,
                                           'min_spent_time': min_spent_time})


def create_issue(request):
    form = IssueForm()

    if request.method == 'POST':
        print(request.POST)
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('get_issues'))
    context = {'form': form}
    return render(request, "issueform.html", context)

def edit_issue(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    if request.method != 'POST':
        form = IssueForm(instance=issue)
    else:
        form = IssueForm(instance=issue, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('get_issues'))
    context = {'issue': issue, 'form': form}
    return render(request, 'issueform.html', context)


#REST API Views

@api_view(['GET'])
def get_issues_rest(request):
    issues_set = Issue.objects.all()
    serializer = IssueSerializer(issues_set, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_issue_by_id_rest(request, id):
    issue = Issue.objects.get(id=id)
    serializer = IssueSerializer(issue)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)
