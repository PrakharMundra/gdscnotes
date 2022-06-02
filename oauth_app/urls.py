from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('',views.index,name='note-index'),
    path('accounts/', include('allauth.urls')),
     path('logout/', auth_views.LogoutView.as_view(template_name='oauth_app/logout.html'), name='logout'),
]
