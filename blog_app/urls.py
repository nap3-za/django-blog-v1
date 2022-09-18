from django.urls import path
from .views import HomeView, PostView, AddPostView, EditPostView, DeletePostView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('posts/', HomeView.as_view(), name="homeview"),
    path('posts/<int:pk>/', PostView.as_view(), name="postview"),
    path('posts/add/', AddPostView.as_view(), name="add-postview"),
    path('post/<int:pk>/edit/', EditPostView.as_view(), name="editpostview"),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name="deletepostview"),
    ]
