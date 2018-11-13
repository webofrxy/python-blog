from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.

def getlist(request):
    # post_list = User.objects.order_by('-pub_date')[:5]
    # output = ','.join([p.title for p in post_list])
    return HttpResponse('getlist部分') 

def getinfo(request):
    return HttpResponse('get部分')