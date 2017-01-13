from django.shortcuts import render, render_to_response
from datetime import datetime
from news.models import NewsFeed
from companies.models import Companies

# Create your views here.

def index(request):
    newsfeed = NewsFeed.objects.all().order_by("id")[::-1]
    return render(request, 'index.html', {'time': datetime.now(), 'news': newsfeed})

def portfolio(request):
	#company = Companies.objects.all()
    return render(request, 'portfolio.html', {'time': datetime.now()})
