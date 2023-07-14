from django.urls import path
from django.contrib.auth import views as auth_views
from user import views

app_name = "user"

urlpatterns = [
    path('', views.mainPage, name='mainPage'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('signupPage/', views.signupPage, name='signupPage'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup')
]
