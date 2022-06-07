from django.urls import path
from .views import PostDeleteView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('startPage/', views.startPage, name='nextgig-startPage'),
    path('', PostListView.as_view(), name='nextgig-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view, name='post-delete'),
    path('post/<int:pk>/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='nextgig-about')
]