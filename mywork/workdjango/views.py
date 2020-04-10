from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
)
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'workdjango/home.html' 
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    success_url = '/'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

    