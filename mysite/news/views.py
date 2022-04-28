from django.http import HttpResponse
from django.shortcuts import render

from .models import *

# Create your views here.
def index(request):
    news = News.objects.order_by('-created_at')
    context={
        'news': news,
        'title': 'news list',

    }
    return render(request, 'news/index.html', context=context)



def test(request):
    return HttpResponse("<h1>daddr</h1>")
