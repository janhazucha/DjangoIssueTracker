from django.shortcuts import render,redirect
from .models import Issue
from .forms import IssueForm
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


def create_issue(request):
    form = IssueForm()

    if request.method == 'POST':
        print(request.POST)
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, "issueform.html", context)




# def create_issue(request):
#     if request.method == "POST":
#         form = IssueForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.instance.author = request.user
#             if form.instance.issue_type == 'FEATURE':
#                 form.instance.price = 100
#             else:
#                 form.instance.price = 0
#             issue = form.save()
#             return redirect(issue_detail, issue.pk)
#     else:
#         form = IssueForm()
#     return render(request, 'issueform.html', {'form': form})