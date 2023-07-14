from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from qna.views import create_question
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


# # 회원가입
# def signup(request):
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)  # 사용자 인증
#
#             login(request, user)  # 로그인
#
#             # 회원가입과 동시에 해당 유저에 해당하는 QnA 생성
#             create_question(user)
#
#             return redirect('user:mainPage')
#     else:
#         form = UserForm()
#     return render(request, 'signup.html', {'form': form})

# 회원가입
def signup(request):
    if request.method == "GET":
        return (request, 'signup.html')
    elif request.method == "POST":
        username = request.POST.get('username', None)
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)
        email = request.POST.get('email', None)
        user = User(
            username=username,
            password=make_password(password1),
        )
        if not (username and email and password1 and password2):
            err_data = '모든 항목을 입력해주세요.'
            return render(request, 'signup.html', context={'error': err_data})

        if User.objects.all().filter(username=request.POST.get('username', None)).exists() == True:
            err_data = '이미 존재하는 아이디입니다.'
            return render(request, 'signup.html', context={'error': err_data})

        if password1 != password2:
            err_data = '비밀번호가 다릅니다.'
            return render(request, 'signup.html', context={'error': err_data})
        else:
            user.save()
            create_question(user)
            return redirect('user:mainPage')






