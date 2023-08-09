from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post

def home(request):
    # Fetch all published blog posts
    posts = Post.objects.filter(published=True)
    return render(request, 'blog/home.html', {'posts': posts})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-publish_date']
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

# Create your views here.
