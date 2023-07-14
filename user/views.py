from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from qna.views import create_question
from user.models import User


# 메인 페이지
def mainPage(request):
    return render(request, 'main.html')

# 로그인 페이지
def loginPage(request):
    return render(request, 'login.html')

# 회원가입 페이지
def signupPage(request):
    return render(request, 'signup.html')

# 로그인
# def login(request):
#     if request.method =='GET':
#         return render(request, 'login.html')
#     elif request.method == 'POST':
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)
#
#         err_data = {}
#         if not(username and password):
#             err_data['error'] = '모든 값을 입력해 주세요.'
#         else:
#             user = User.objects.get(username=username)
#             if check_password(password, user.password):
#                 request.session['user'] = user.id
#                 return redirect('user:mainPage')
#             else:
#                 err_data['error'] = '비밀번호가 일치하지 않습니다.'
#         return render(request, 'login.html', err_data)

def signup(request):
    if request.method == "GET":
        return (request, 'signup.html')

    elif request.method == "POST":
        username = request.POST.get('username', None)
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)

        user = User(
            username=username,
            password=make_password(password1)
        )
        if not (username and password1 and password2):
            err_data = '모든 항목을 입력해주세요.'
            return render(request, 'signup.html', context={'error': err_data})

        if User.objects.all().filter(username=username).exists() == True:
            err_data = '이미 존재하는 아이디입니다.'
            return render(request, 'signup.html', context={'error': err_data})

        if password1 != password2:
            err_data = '비밀번호가 다릅니다.'
            return render(request, 'signup.html', context={'error': err_data})

        else:
            user.save()
            create_question(user)

            return redirect('user:mainPage')






