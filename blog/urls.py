from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('join/', views.join, name = 'join'),
    path('/', views.sign_in, name = 'sign_in'),
    path('log_out/', views.log_out, name= 'log_out'),


]