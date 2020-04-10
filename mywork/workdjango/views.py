from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
   
)
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'workdjango/home.html' 
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    success_url = '/'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

class PostDetailView(DetailView):
    model = Post     