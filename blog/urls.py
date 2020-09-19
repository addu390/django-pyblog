from django.urls import path
from . import views

urlpatterns = [
    path('posts', views.index, name='posts'),
    path('posts/<str:post_id>/', views.post, name='post'),
]