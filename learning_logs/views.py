from django.shortcuts import render, redirect

from .models import Topic

def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')