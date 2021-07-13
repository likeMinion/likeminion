from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    # 7월 13일
    path('create/', AccountCreateView.as_view(), name='create') # 2번째 인자는 view 인자를 넣어야함
]