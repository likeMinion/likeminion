from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    # 7월 13일
    path('create/', AccountCreateView.as_view(), name='create'), # 2번째 인자는 view 인자를 넣어야함
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # 7월 15일
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'), # <int:pk> 추가적인 정보 / pk:primary key value

    # 7월 19일
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update')
]