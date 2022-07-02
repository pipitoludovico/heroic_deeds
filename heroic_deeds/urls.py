""" Defines URL patterns for heroic deeds"""

from django.urls import path
from . import views

app_name = 'heroic_deeds'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Topics Page
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]
