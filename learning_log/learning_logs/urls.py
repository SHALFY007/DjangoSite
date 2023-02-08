"""Add a pattern URL of learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page with  list of topics
    path('topics/', views.topics, name='topics'),
    # Page with topic
    path('topics/<int:topic_id>', views.topic, name='topic')
]