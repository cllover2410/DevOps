from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse # 每个视图函数第一个参数第一是request，且必须返回HttpResponse对象

def index(request):
  return HttpResponse(u"123456")

def withparam(request, year=12, month=21): # 带参数的视图函数
  return HttpResponse("This is with param {0},{1}".format(year, month))