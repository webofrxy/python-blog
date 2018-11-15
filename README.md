# python-blog

## 环境：
- python 3.6.0
- django 2.0.1

## django 使用经验
django是python下一款功能比较全面的框架，它有以下一些特点
### 支持数据库的ORM操作
使用方法如下：
```python
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from blog.models import User

# Create your views here.

def get_user_list(request):
    userlist = User.objects.all()
    return HttpResponse(userlist) 

def delete_user_info(request):
    id = request.POST.get('id')
    User.objects.filter(id=id).delete()
    return HttpResponse('删除成功')

def add(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    info = User(name=name, description=description)
    data = info.save()
    return HttpResponse('插入成功')
```
### 支持缓存系统
Django和memcached、redis或者其他的缓存系统联用，可以提高页面的加载速度。
### 具有模板系统
Django的模板对于开发普通网站来说基本够用。