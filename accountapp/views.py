from django.http import HttpResponse, HttpResponseRedirect
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
from django.urls import reverse

from accountapp.models import HelloWorld


# def hello_world(request):
#     if request.method == 'POST':
#
#         temp = request.POST.get('input_text') # request 안에 POST 내의 값을 가져옴
#
#         new_hello_world = HelloWorld()
#         new_hello_world.text = temp
#         new_hello_world.save() # 데이터 베이스 안에 새로운 행이 만들어짐
#
#         hello_world_list = HelloWorld.objects.all() # 모든 데이터를 가져옴
#
#         # return render(request, 'accountapp/hello_world.html',
#         #               context={'new_hello_world': new_hello_world}) # new_hello_world라는 객체를 넘겨줌
#         return render(request, 'accountapp/hello_world.html',
#                       context={'hello_world_list': hello_world_list})
#     else:
#         hello_world_list = HelloWorld.objects.all()  # 모든 데이터를 가져옴
#         return render(request, 'accountapp/hello_world.html',
#                       context={'hello_world_list':hello_world_list})

from accountapp.models import HelloWorld
def hello_world(request):
    if request.method == 'POST':
        temp = request.POST.get('input_text')  # request 안에 POST 내의 값을 가져옴
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()  # 데이터 베이스 안에 새로운 행이 만들어짐

        # Get 부분과 중복되는 코드 삭제함
        # 실행해서 페이지에서 새로고침할 때 중복 코드 입력되는 것을 방지함
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()  # 모든 데이터를 가져옴
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})

# 7월 13일
from django.views.generic import CreateView, DetailView
from django.contrib.auth.models import User # ctrl + b / 누르면 선언한 곳으로 이동, 파악가능
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') # 함수형과 클래스형이 부르는 방식이 다름
    template_name = 'accountapp/create.html' #

# 7월 15일
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'