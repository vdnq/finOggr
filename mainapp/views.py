from django.shortcuts import render, render_to_response
from datetime import datetime
from news.models import NewsFeed

# Create your views here.

def index(request):
    newsfeed = NewsFeed.objects.all()
    return render_to_response('index.html', {'time': datetime.now(), 'news': newsfeed})

def portfolio(request):
    return render_to_response('portfolio.html', {'time': datetime.now()})
