from django.db.models.signals import post_save
from django.dispatch import receiver

from qna.models import QnA
from user.models import User


@receiver(post_save, sender=User)
def create_user_posts(sender, instance, created, **kwargs):
    if created:
        # 사용자가 새로 생성되었을 때 실행될 로직
        # 매핑된 게시글 생성 등의 작업을 수행
        QnA.objects.create(user=instance, title='제목1')
        QnA.objects.create(user=instance, title='제목2')
        QnA.objects.create(user=instance, title='제목3')