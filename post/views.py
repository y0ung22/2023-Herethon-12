from datetime import timezone

from django.shortcuts import render, redirect

from post.models import Post


# 전체 게시글 조회
def post_list(request):
    if request.user.is_staff:
        posts = Post.objects.all()
        return render(request, 'post_list.html', context={'posts': posts})

    return redirect('user:mainPage')

# 게시글 생성
def post_create(request):
    if not request.user.is_authenticated:
        return redirect('user:mainPage')

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

# 상세 게시글 조회
def post_detail(request, pk):
    if not request.user.is_authenticated:
        return redirect('user:mainPage')

    post = Post.objects.get(pk=pk)
    return render(request, 'post_detail.html', context={'post': post})

# 게시글 수정
def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('post:post_list')
    else:
        return render(request, 'post_create.html', context={'post': post})

# 게시글 삭제
def post_delete(request, pk):
    posts = Post.objects.all()

    if request.method == 'GET':
        post = Post.objects.get(pk=pk)
        post.delete()
    return render(request, 'post_list.html', context={'posts': posts})