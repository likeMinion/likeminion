from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    return HttpResponse('Hello World')  # 철자 주의할 것 / alt+Enter하면 모듈을 알아서 가져올 수 있음