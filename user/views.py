from django.contrib.auth import authenticate, login
from django.db.models.signals import post_save
from django.shortcuts import render, redirect

from qna.views import create_question
from user.forms import UserForm
from user.models import User


# 메인 페이지
def mainPage(request):
    #return render(request, 'user/main.html')
    return render(request, 'main.html')

# 로그인 페이지
def loginPage(request):
    #return render(request, 'user/main.html')
    return render(request, 'login.html')

# 회원가입 페이지
def signupPage(request):
    #return render(request, 'user/main.html')
    return render(request, 'signup.html')


# 회원가입
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증

            login(request, user)  # 로그인

            # 회원가입과 동시에 해당 유저에 해당하는 QnA 생성
            create_question(user)

            return redirect('user:mainPage')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})






