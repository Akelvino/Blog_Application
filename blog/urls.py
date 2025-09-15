from django.urls import path 
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('detail/<int:pk>/', views.details, name='deiails'),
    path('new_post/', views.post_new, name='post_new'),
]