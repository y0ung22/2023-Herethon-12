from django.db import models

from user.models import User


class QnA(models.Model):
    index = models.IntegerField() # 인덱스
    question = models.TextField(blank=False) # 질문
    answer = models.TextField(blank=True) # 답변
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 유저 매핑

    def __str__(self):
        return self.question



