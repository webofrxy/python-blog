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

class ArticleListView(ListView):
    # 页面类型 分类目录或标签列表
    page_type = ''
    page_kwarg = 'page'
    link_type = '1'

    def get_view_cache_key(self):
        return self.request.get['page']
    
    @property
    def page_num(self):
        page_kwarg = self.page_kwarg
        page = self.kwarg.get(page_kwarg) or self.request.GET.get(page_kwarg) or 1
        return page 
    
    def get_queryset_cache_key(self):
        """
        子类重写，获得queryset的缓存key
        """
        