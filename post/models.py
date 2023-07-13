from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User=get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE) # 유저 매핑
