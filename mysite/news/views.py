from django.http import HttpResponse
from django.shortcuts import render

from .models import *

# Create your views here.
def index(request):
    news = News.objects.all()
    context={
        'news': news,
        'title': 'news list',

    }
    return render(request, 'news/index.html', context=context)




