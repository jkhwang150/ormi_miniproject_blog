from django.http import HttpResponseRedirect,Http404
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CommentForm
from accounts.models import User



# Create your views here.
def postlist(request):
    boards = {'boards': Board.objects.all()}
    return render(request, 'postlist/postlist.html', boards)

@login_required
def post(request):
    if request.method == "POST":
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        board = Board(author=author, title=title, content=content)
        board.save()
        return redirect('postlist')
    else:
        return render(request, 'postlist/post.html')
    
def postdetail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
        comments = CommentForm()
        comment_view = Comment.objects.filter(post=pk)
    except Board.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'postlist/postdetail.html', {'board': board, 'comments':comments, 'comment_view':comment_view})

@login_required
def edit(request,pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'postlist/edit.html', {'board' :board})

@csrf_exempt
def update(request, pk):
    update_post = Board.objects.get(pk=pk)
    update_post.author = request.POST.get('author')
    update_post.title = request.POST.get('title')
    update_post.content = request.POST.get('content')
    update_post.save()

    return redirect('postlist')

@login_required
@csrf_exempt
def delete(request,pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('postlist')

def comment(request,pk):
    comment = CommentForm(request.POST)
    if comment.is_valid():
        comments = comment.save(commit=False)
        comments.post = get_object_or_404(Board, pk=pk)
        comments.save()
    return redirect('postdetail', pk)