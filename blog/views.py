# blog/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
import calendar

# View for displaying the list of posts
def post_list(request):
    # Fetch posts, ordered by published date
    posts = Post.objects.all().order_by('-published_date')
    years = Post.objects.values('published_date__year').distinct().order_by('published_date__year')

    # Loop over each year 
    years_and_months = {}
    for year in years:
        months = Post.objects.filter(published_date__year=year['published_date__year']) \
            .values('published_date__month') \
            .distinct().order_by('published_date__month')
        
        # For each year, store a list of months
        years_and_months[year['published_date__year']] = [
            {
                'month': month['published_date__month'],
                'month_name': calendar.month_name[month['published_date__month']]
            } for month in months
        ]

    # Get selected year and month
    selected_year = request.GET.get('year')
    selected_month = request.GET.get('month')

    if selected_year:
        posts = posts.filter(published_date__year=selected_year)
    if selected_month:
        posts = posts.filter(published_date__month=selected_month)

    posts = posts.order_by('published_date')

    context = {
        'posts': posts,
        'years_and_months': years_and_months,
        'selected_year': selected_year,
        'selected_month': selected_month,
    }

    return render(request, 'blog/post_list.html', context)

# Creating new posts
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new post to the database
            return redirect('post_list')  # Redirect to a page where posts are listed
    else:
        form = PostForm()  # Display the empty form

    return render(request, 'blog/create_post.html', {'form': form})

# Displaying the posts
def post_detail(request, pk):
    # Retrieve the post by its primary key (pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# View for confirming and deleting posts
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk) # Retrieve the post to delete
    if request.method == "POST":
        post.delete()
        return redirect('post_list')  # Redirect to the post list after deleting
    return render(request, 'blog/post_confirm_delete.html', {'post': post})