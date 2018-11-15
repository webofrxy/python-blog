from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from blog.models import User

# Create your views here.

def get_user_list(request):
    userlist = User.objects.all()
    return HttpResponse(userlist) 

def get_user_info(request):
    id = request.POST.get('id')
    User.objects.filter(id=id).delete()
    return HttpResponse('删除成功')

def add(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    info = User(name=name, description=description)
    data = info.save()
    return HttpResponse('插入成功')


    
