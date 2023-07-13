from django.urls import path

from post import views

app_name = "post"

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('<int:pk>/detail', views.post_detail, name='post_detail'),
    path('<int:pk>/edit', views.post_edit, name='post_edit'),
    path('<int:pk>/delete', views.post_delete, name='post_delete'),
]