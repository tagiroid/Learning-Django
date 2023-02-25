"""URLs for users paths"""

from django.urls import path, include
from . import views


app_name = 'users'
urlpatterns = [
    # URL for authorization by default
    path('', include('django.contrib.auth.urls')),
    # registration page
    path('register/', views.register, name='register'),
]