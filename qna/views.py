from django.shortcuts import redirect, get_object_or_404, render

from qna.models import QnA


# 답변 등록 = 게시글 수정
def write_answer(request, index):
    user = request.user

    if not user.is_authenticated:
        return redirect('user:mainPage')  # 로그인하지 않으면 로그인창 이동, 로그인하면 질문

    if request.method == "POST":
        qna = get_object_or_404(QnA, index=index, user=user)

        answer = request.POST.get('answer')

        # 데이터 변경
        qna.answer = answer
        user.qrecord = index + 1

        qna.save()
        user.save()


        if qna.answer == '':
            return render(request, 'reply.html', context={'qna': qna})
        else:
            if not index == 31:  # 숫자는 마지막 게시글 인덱스와 같도록
                nextqna = get_object_or_404(QnA, index=index + 1, user=user)

                if index == 3:  # colors 이미지 나오기 전 질문 인덱스 -> 4번 질문 답하면 colors1
                    return render(request, 'colors1.html', context={'qna': nextqna})  # 다음 qna 보여줌
                if index == 14:  # colors 이미지 나오기 전 질문 인덱스 -> 15번 질문 답하면 colors2
                    return render(request, 'colors2.html', context={'qna': nextqna})
                if index == 22:  # colors 이미지 나오기 전 질문 인덱스 -> 23번 질문 답하면 colors3
                    return render(request, 'colors3.html', context={'qna': nextqna})
                if index == 28:  # colors 이미지 나오기 전 질문 인덱스 -> 29번 질문 답하면 colors4
                    return render(request, 'colors4.html', context={'qna': nextqna})

                return render(request, 'question.html', context={'qna': nextqna})  # 일반 질문일 경우 다음 qna 보여줌

            else:  # 마지막 게시글이라면 colors5로 이동
                user.is_staff = True
                user.save()
                return render(request, 'colors5.html')

    return redirect('user:mainPage') # get요청시 메인 페이지로

# 나레이션 -> 질문 페이지 or 답변페이지에서 완료버튼 -> 질문 페이지
def show_question(request, qrecord):
    user = request.user

    if not user.is_authenticated:
        return redirect('user:mainPage')  # 로그인하지 않으면 로그인창 이동, 로그인하면 질문

    if request.method == "POST":
        qna = get_object_or_404(QnA, index=qrecord, user=user)
        return render(request, 'question.html', context={'qna': qna})

    return redirect('user:mainPage') # get요청시 메인 페이지로

# 질문 페이지 -> 답변 페이지 - 완료 버튼 > 다음 질문 페이지
def show_answer(request, index):
    user = request.user

    if not user.is_authenticated:
        return redirect('user:mainPage')  # 로그인하지 않으면 로그인창 이동, 로그인하면 질문

    if request.method == "POST":
        qna = get_object_or_404(QnA, index=index, user=user)
        return render(request, 'reply.html', context={'qna': qna})

    return redirect('user:mainPage') # get요청시 메인 페이지로


# 서비스 경험 여부에 따른 렌더
def start(request):
    user = request.user

    if user.is_authenticated:
        if request.method == "POST":
            if user.qrecord == 32: # 모든 질문 답변 완료
                user.is_staff = True
                user.save()
                return render(request, 'toPost.html')

            if user.qrecord == 0: # 첫 사용자라면 나레이션으로
                return render(request, 'narration.html', context={'user': user})
            else:
                qna = get_object_or_404(QnA, index=user.qrecord, user=user)
                return render(request, 'question.html', context={'qna': qna}) # 아니라면

        return redirect('user:mainPage')  # get요청시 메인 페이지로

    return redirect('user:mainPage') # get요청시 메인 페이지로

def toPage(request, pIndex):

    if request.method == 'POST':
        if pIndex == 5: # colors5.html 이라면
            return render(request, 'colors6.html')
        if pIndex == 6: # colors6.html 이라면
            return render(request, 'ending.html')
        if pIndex == 7: # ending.html 이라면
            return render(request, 'toPost.html')

    return redirect('user:mainPage')

# QnA 객체 생성
def create_question(user):
#감각 깨우기
    QnA.objects.create(index=0, question='그런데 지금 어디에 계시나요? 창문 너머를 바라보세요. 시선을 멀리 두세요. 아니요, 방금 바라본 것보다 더 멀리. 무엇이 보이시나요?', user=user)
    QnA.objects.create(index=1, question='당신이 어떻게 숨을 쉬는지 알고 계시나요? 눈을 감고 숨소리에 집중해보세요. 어떻게 숨을 쉬고 계시나요?', user=user)
    QnA.objects.create(index=2, question='숨을 쉬었더니 향기가 느껴집니다. 한 번 더 눈을 감아주세요. 어떤 향기가 나고 있죠?', user=user)
    QnA.objects.create(index=3, question='이제 나를 내려두세요. 오른손으로 왼손을 느껴봅시다. 천천히.', user=user)
    QnA.objects.create(index=4, question='다음은 손바닥을 맞대어 문질러주세요. 따뜻해질 정도로요. 이 순간 당신을 둘러싼 공기는 얼마나 따뜻하거나 차갑나요?', user=user)

#(인간관계)
    QnA.objects.create(index=5, question='당신에게 중요한 사람들은 누구인가요? 왜 그들이 당신에게 중요하다고 생각하세요?', user=user)
    QnA.objects.create(index=6, question='당신의 감정과 경험에 응원을 보내줄 수 있는 사람은 누구인가요? 가족, 친구, 동료.. 누구라도 될 수 있을 겁니다.', user=user)
    QnA.objects.create(index=7, question='요즘 당신이 가장 지지 받고 싶은 생각이 있으실 거에요. 어떤 지지를 받고 싶으세요? 포옹, 응원의 말, 묵묵히 지켜봐주는 것… 무엇이든지요!', user=user)
    QnA.objects.create(index=8, question='혹시 당신의 의견이나 감정을 표현하는 데 어려움을 겪고 있으시다면 어떤 어려움이나 불편함인지 말해주실래요?', user=user)
    QnA.objects.create(index=9, question='당신이 원하는 이상적이고 만족스러운 관계는 어떤 모습인가요?', user=user)
    QnA.objects.create(index=10, question='혹시 단절이 필요하다고 느끼시나요? 무엇으로부터?', user=user)
#(진로 및 목표)
    QnA.objects.create(index=11, question='요즘 당신은 무얼 하고 지내시나요?', user=user)
    QnA.objects.create(index=12, question='당신이 요즘 가장 흥미 있는 분야는 무엇인가요?', user=user)
    QnA.objects.create(index=13, question='학업에 집중하는 것이 힘들게 느껴지나요? 어떤 점에서 그렇게 느끼시는지 알려주세요.', user=user)
    QnA.objects.create(index=14, question='당신이 가지고 있는 ‘희망’이 궁금해요. 어떤 희망을 가지고 계시나요?', user=user)
    QnA.objects.create(index=15, question='당신이 가진 희망에 대해 얼마나 자신감을 가지고 계세요?', user=user)

#(강박)
    QnA.objects.create(index=16, question='요즘 당신이 자주 사용하는 말이나 단어는 없나요? 나는 이미 알고 있지만 당신은 모를 수도 있어요. 천천히 생각해보세요.', user=user)
    QnA.objects.create(index=17, question='당신이 실패나 실수했을 경우, 어떻게 반응하고 계시나요?', user=user)
    QnA.objects.create(index=18, question='더 나은 사람이 되기 위해 스스로 억압하고 있는 부분은 무엇일까요?', user=user)
    QnA.objects.create(index=19, question='일상 속에서 당신이 ‘여성’이기 때문에 겪는 어려움이 있나요? 있다면 무엇인가요?', user=user)
    QnA.objects.create(index=20, question='완벽하고 더 나은 상태가 되어야 한다는 생각이 당신의 학업과 일상에 어떤 영향을 미치는지 알려주세요.', user=user)
    QnA.objects.create(index=21, question='혹시 당신이 ‘여성’이기 때문에 더 완벽해야 한다고 생각하실 때도 있나요?', user=user)
    QnA.objects.create(index=22, question='완벽하지 않은 나를 사랑하고 받아들일 수 있는 방법이 있을까요? 지금 당장은 어려울 수도 있겠지만요.', user=user)
    QnA.objects.create(index=23, question='혹시 휴식이 필요하다고 느끼시나요? 무엇으로부터?', user=user)

#(나에 대해 알기)
    QnA.objects.create(index=24, question='요즘 당신을 괴롭히는 것은 무엇인가요?', user=user)
    QnA.objects.create(index=25, question='당신 삶의 우선순위를 살펴보겠습니다. 맨 아래에서부터요. 요즘 당신의 삶에서 거들떠보지도 않고 신경 쓰지도 못하는 것은 무엇인가요?', user=user)
    QnA.objects.create(index=26, question='반대로 요즘 당신의 마음을 차지한 1순위는 무엇인가요? 나였으면 좋겠지만 괜찮아요. 천천히 생각해보세요.', user=user)
    QnA.objects.create(index=27, question='당신의 삶에서 가장 중요한 가치는 무엇인가요? 당신을 행동하게 만드는 무언가를 말하는 겁니다.', user=user)
    QnA.objects.create(index=28, question='어떤 상황에서 가장 행복하다고 느끼시나요? 그 순간을 더 자주 경험하기 위해 무엇을 할 수 있을까요?', user=user)
    QnA.objects.create(index=29, question='당신의 삶을 설명할 수 있는 단어나 말이 있다면 무엇일까요. 당신의 삶을 지배하고 있는 단어 같은 거 있잖아요.', user=user)

    QnA.objects.create(index=30, question='내일 어떤 하루가 펼쳐지기를 원하시나요?', user=user)
    QnA.objects.create(index=31, question='나는 어떤 사람일까요? 여기서 ‘나’는 당신을 말하는 거에요.', user=user)