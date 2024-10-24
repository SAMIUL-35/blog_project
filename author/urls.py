
from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.register ,name='register'),
    path('login/', views.user_login ,name='login'),
    path('logout/', views.User_logout ,name='logout'),
    path('profile/', views.profile ,name='profile'),
    path('profile/edit/', views.edit_profile ,name='edit_profile'),
    path('profile/edit/change_pass/', views.change_pass ,name='change_pass'),
   
]
