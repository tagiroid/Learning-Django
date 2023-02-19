from django.shortcuts import render
from .models import Topic
# Create your views here.


def index(request):
    """learning_logs homepage"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    # shows list of topics
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
