from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('about/', about, name='about'),
    path('tracks/',tracking, name='track'),
    path('ask/', ask, name='ask'),
    path('questions/', questions, name="questions"),
    path('answer/<int:askid>', answer, name='answer'),
    path('blogs/', posts, name='post'),
    path('blog/<slug:slug>/', postDetail, name="post-detail"),
]
