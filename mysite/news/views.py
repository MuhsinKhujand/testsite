from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('fff')

def test(request):
    return HttpResponse("<h1>dfdfdfd</h1>")