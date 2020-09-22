from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('posts/<int:page_id>/', views.index, name='posts'),
    path('posts/<str:post_id>/', views.post, name='post'),
    path('search/', views.search, name='search'),
    path('category/', views.search_category, name='category'),
    path('contact/', views.contact, name='contact'),
]