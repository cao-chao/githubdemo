from django.shortcuts import render,HttpResponse

# Create your views here.


def index(request):
    # 第一次写项目
    # 创建了一个dev分支
    return HttpResponse("好紧张")