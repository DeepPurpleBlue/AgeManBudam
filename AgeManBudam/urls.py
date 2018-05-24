"""AgeManBudam URL Configuration
"""
from django.contrib import admin
from django.urls import path
from AgeManBudamApi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('submit-post',views.submit_post),
    path('submit-like',views.submit_like),
    path('get-posts',views.get_posts)
]
