from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# 7월 26월
class Profile(models.Model):
    # CASCADE : 종속
    # 삭제됐을 때 종속된 모델도 같이 삭제한다는 의미
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=30, unique=True, null=True)
    message = models.CharField(max_length=200, null=True)
