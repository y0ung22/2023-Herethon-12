from django.contrib.auth import login, authenticate
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


def custom_login(request):
    if request.method == "GET":
        return (request, 'login.html')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not (username and password):
            err_data = '모든 항목을 입력해주세요.'
            return render(request, 'login.html', context={'error': err_data})

        if not User.objects.all().filter(username=username).exists() == True: # username이 존재하지 않는다면
            err_data = '존재하지 않는 아이디입니다.'
            return render(request, 'login.html', context={'error': err_data})

        else: # 아이디가 존재하면
            existUser = User.objects.get(username=username)

            if not password == existUser.password: # 입력한 username을 가진 기존 User 객체의 password와 입력한 pssword가 다르다면
                err_data = '비밀번호를 잘못 입력하였습니다.'
                return render(request, 'login.html', context={'error': err_data})
            else: # 비밀번호가 같으면
                #user = authenticate(request, username=username, password=password)
                login(request, authenticate(request, username=username, password=password)) # 로그인
                return redirect('user:mainPage')

def signup(request):
    if request.method == "GET":
        return (request, 'signup.html')

    elif request.method == "POST":
        username = request.POST.get('username', None)
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)

        user = User(
            username=username,
            password=password1,
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






