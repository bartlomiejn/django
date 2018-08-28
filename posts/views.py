from django.shortcuts import render
from .models import Post
from django.views.generic.list import ListView

class HomePageView(ListView):
    model = Post
    template_name = 'posts/home.html'