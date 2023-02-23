"""URL users"""

from django.urls import path, include

from . import views

app_name = "users"

urlpatterns = [
    # Turn on URL sign up default
    path('', include('django.contrib.auth.urls')),
    # register page
    path('register/', views.register, name='register'),
]