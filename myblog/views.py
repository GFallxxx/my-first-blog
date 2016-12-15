from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, BlogComment
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

'''
nota bene: Each view function takes at least one parameter, called request by convention.
This is an object that contains information about the current Web request that has triggered this view, and is an instance of the class django.http.HttpRequest.

The main lesson here is this: a view is just a Python function that takes an HttpRequest as its first parameter and returns an instance of HttpResponse.
p.es.
from django.http import HttpResponse
def hello(request):
    return HttpResponse("Hello world")
'''
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'myblog/post_list.html', {'posts': posts} )

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            #se non valorizzo il campo post.published_date il post non viene autom. pubblicato
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk = post.pk)
    else:
        form = PostForm()
    return render(request, 'myblog/post_edit.html', {'form':form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'myblog/post_detail.html', {'post': post} )

@login_required
def post_draft(request):
    posts = Post.objects.filter(published_date__isnull=True)
    return render(request, 'myblog/post_draft.html', {'posts': posts} )

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.published_date = timezone.now()
    post.save()
    return redirect('post_list')

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

@login_required
def post_unpublish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.published_date = None
    post.save()
    return redirect('post_list')

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk = post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'myblog/post_edit.html', {'form':form})

@login_required
def comment_new(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # salva in comment i campi passati dal form
            #comment.author = form.author
            comment.created_date = timezone.now()
            comment.post = post
            comment.approved_comment = False
            comment.save()
            return redirect('post_detail', pk = post.pk)
    else:
        form = CommentForm()
    return render(request, 'myblog/comment_edit.html', {'form':form})

@login_required
def comment_publish(request, pk):
    comment = get_object_or_404(BlogComment, pk=pk)
    comment.approve()
    comment.save()
    return redirect('post_detail', pk = comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(BlogComment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk = comment.post.pk)

@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(BlogComment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance = comment)
        if form.is_valid():
            comment.approved_comment = False
            form.save()
            return redirect('post_detail', pk = comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'myblog/comment_edit.html', {'form':form})
