from django.shortcuts import render
from .models import Issue
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_issues(request):

    list_of_issues = Issue.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(list_of_issues, 20)
    try:
        issues = paginator.page(page)

    except PageNotAnInteger:

        issues = paginator.page(1)

    except EmptyPage:

        issues = paginator.page(paginator.num_pages)

    return render(request, "issues.html", {'issues': issues})