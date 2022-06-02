from django.urls import path
from . import views
from .views import UserPostListView,PostCreateView,PostUpdateView,PostDeleteView,PostDetailView
urlpatterns = [
      path('user/<username>/', UserPostListView.as_view(), name='note-home'),
      path('note/new/',PostCreateView.as_view(),name='note-create'),
      path('note/<int:pk>/update/',PostUpdateView.as_view(),name='note-update'),
      path('note/<int:pk>/delete/',PostDeleteView.as_view(),name='note-delete'),
      path('note/<int:pk>/', PostDetailView.as_view(), name='note-detail'),
]