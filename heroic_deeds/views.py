from django.shortcuts import render
from .models import Topic


def index(request):
    """The home of heroic_deeds"""
    return render(request, 'heroic_deeds/index.html')


def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'heroic_deeds/topics.html', context)


def topic(request, topic_id):
    """Show single topic and its entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'heroic_deeds/topic.html', context)
