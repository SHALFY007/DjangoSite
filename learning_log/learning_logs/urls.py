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
    path('topics/<int:topic_id>', views.topic, name='topic'),
    # Page where user can add topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Add new Entries
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry')
]