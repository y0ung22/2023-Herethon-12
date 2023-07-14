from django.urls import path
from user import views

app_name = "user"

urlpatterns = [
    path('', views.mainPage, name='mainPage'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('signupPage/', views.signupPage, name='signupPage'),
    path('login/', views.custom_login, name='custom_login'),
    path('signup/', views.signup, name='signup')
]
