from django.shortcuts import render, render_to_response
from datetime import datetime

# Create your views here.

def index(request):
    return render_to_response('index.html', {'time': datetime.now()})
