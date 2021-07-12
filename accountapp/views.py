from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# 6월 28일
#def hello_world(request):
#    return HttpResponse('Hello World')  # 철자 주의할 것 / alt+Enter하면 모듈을 알아서 가져올 수 있음

# 7월 1일
# def hello_world(request): # request : 어디서 요청이 들어왔는지 알 수 있음
#     return render(request, 'base.html')

# 7월 5일
# def hello_world(request):
#     return render(request, 'accountapp/hello_world.html')

# 7월 8일
# def hello_world(request):
#     if request.method == 'POST':
#         return render(request, 'accountapp/hello_world.html',
#                       context={'text':'POST METHOD'})
#     else:
#         return render(request, 'accountapp/hello_world.html',
#                       context={'text':'GET METHOD'})

# 7월 12일
def hello_world(request):
    if request.method == 'POST':

        temp = request.POST.get('input_text') # request 안에 POST 내의 값을 가져옴

        return render(request, 'accountapp/hello_world.html',
                      context={'text': temp}) # POST METHOD
    else:
        return render(request, 'accountapp/hello_world.html',
                      context={'text':'GET METHOD'})