from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Count

# Create your views here.

def home(request):
	cust =Customer.objects.all()
	issue =Issue.objects.all()
	total_issue = issue.count()
	open_issue = issue.filter(status='Open').count()
	closed_issue = issue.filter(status='Closed').count()
	#issue_count = Issue.objects.values('Customer_name').annotate(Count('Customer_name'))
	issue_count = issue.filter(id=2)
	#cust_issue =cust.iss
	context = {'cust' :cust, 'total_issue' :total_issue, 'open_issue' :open_issue, 'closed_issue' :closed_issue, 'issue' :issue, 'issue_count' :issue_count}
	return render(request, 'accounts/dashboard.html', context)

def customer(request, pk_test):
    cutomer = Customer.objects.get(id=pk_test)
    issues = cutomer.issue_set.all()
    count = issues.count()
    context = {'customer' : cutomer, 'issues': issues, 'count':count}

    return render(request, 'accounts/customer.html', context)

def Issues(request):
    issues =Issue.objects.all()
    content = {'issues' :issues}
    return render(request, 'accounts/Issue.html', content)
