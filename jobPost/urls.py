from django.urls import path

from jobPost import views

urlpatterns = [
    path('posts/', views.get_post, name='Posts'),
    path('create/', views.make_post, name='Create'),
]