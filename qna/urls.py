from django.urls import path
from qna import views

app_name = "qna"

urlpatterns = [
    path('', views.start, name='start'), # 첫사용자라면 나레이션 이동, 기사용자라면 답변하지 않은 질문 페이지로 이동
    path('<int:index>/write/', views.write_answer, name='write_answer'), # 답변
    path('<int:qrecord>/question/', views.show_question, name='show_question'),
    path('<int:index>/answer/', views.show_answer, name='show_answer')
]