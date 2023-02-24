"""URLs for users paths"""

from django.urls import path, include


app_name = 'users'
urlpatterns = [
    # URL for authorization by default
    path('', include('django.contrib.auth.urls')),
]