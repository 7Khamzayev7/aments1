from django.shortcuts import render
from blog.models import Author, Post
from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Count
from django.urls import reverse
from django.shortcuts import get_object_or_404
from blog.forms import CommentForm

class Blog(ListView):
    template_name = 'blog.html'

