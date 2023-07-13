from django.shortcuts import redirect, get_object_or_404, render

from qna.models import QnA


# 답변 등록 = 게시글 수정
def write_answer(request, index):
    user = request.user

    if not user.is_authenticated:
        return redirect('user:loginPage')  # 로그인하지 않으면 로그인창 이동, 로그인하면 질문

    if request.method == "POST":
        qna = get_object_or_404(QnA, index=index, user=user)


        answer = request.POST.get('answer')

        # 데이터 변경
        qna.answer = answer
        user.qrecord = index+1

        qna.save()
        user.save()

        if not answer is None:
            if not qna.index == 3: # 숫자는 마지막 게시글 인덱스와 같도록
                nextqna = get_object_or_404(QnA, index=index + 1, user=user)
                return render(request, 'question.html', context={'qna': nextqna})  # 다음 qna 보여줌
            else: # 마지막 게시글이라면 방명록 이동 버튼 존재하는 페이지로 이동
                return render(request, 'toPost.html')
        else:
            return render(request, 'reply.html', context={'qna': qna})

    return redirect('user:mainPage') # get요청시 메인 페이지로

# 나레이션 -> 질문 페이지 or 답변페이지에서 완료버튼 -> 질문 페이지
def show_question(request, qrecord):
    user = request.user

    if not user.is_authenticated:
        return redirect('user:loginPage')  # 로그인하지 않으면 로그인창 이동, 로그인하면 질문

    if request.method == "POST":
        qna = get_object_or_404(QnA, index=qrecord, user=user)
        return render(request, 'question.html', context={'qna': qna})

    return redirect('user:mainPage') # get요청시 메인 페이지로

# 질문 페이지 -> 답변 페이지 - 완료 버튼 > 다음 질문 페이지
def show_answer(request, index):
    user = request.user

    if not user.is_authenticated:
        return redirect('user:loginPage')  # 로그인하지 않으면 로그인창 이동, 로그인하면 질문

    if request.method == "POST":
        qna = get_object_or_404(QnA, index=index, user=user)
        return render(request, 'reply.html', context={'qna': qna})

    return redirect('user:mainPage') # get요청시 메인 페이지로


# 서비스 경험 여부에 따른 렌더
def start(request):
    user = request.user

    if user.is_authenticated:
        if request.method == "POST":

            if user.qrecord == 4:
                return render(request, 'toPost.html')

            if user.qrecord == 0: # 첫 사용자라면 나레이션으로

                return render(request, 'narration.html', context={'user': user})
            else:
                qna = get_object_or_404(QnA, index=user.qrecord, user=user)
                return render(request, 'question.html', context={'qna': qna}) # 아니라면
        return redirect('user:mainPage')  # get요청시 메인 페이지로

    return redirect('user:mainPage') # get요청시 메인 페이지로

# QnA 객체 생성
def create_question(user):
    QnA.objects.create(index=0, question='질문1', user=user)
    QnA.objects.create(index=1, question='질문2', user=user)
    QnA.objects.create(index=2, question='질문3', user=user)
    QnA.objects.create(index=3, question='질문4', user=user)














