from datetime import timezone

from django.shortcuts import render, redirect

from post.models import Post


# 전체 게시글 조회
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', context={'posts': posts})

# 게시글 생성
def post_create(request):
    if not request.user.is_authenticated:
        return redirect('user:loginPage')

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        writer = request.user

        Post.objects.create(
            title = title,
            content = content,
            writer = writer,
        )

        return redirect('post:post_list')

    return render(request, 'post_create.html')