# blog/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post

def post_list(request):
    # Retrieve all posts from the database
    posts = Post.objects.all().order_by('-published_date')  # Ordering by published_date in descending order
    return render(request, 'blog/post_list.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new post to the database
            return redirect('post_list')  # Redirect to a page where posts are listed
    else:
        form = PostForm()  # Display the empty form

    return render(request, 'blog/create_post.html', {'form': form})

def post_detail(request, pk):
    # Retrieve the post by its primary key (pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})