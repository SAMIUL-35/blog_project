
from django.urls import path
from .import views

urlpatterns = [
    path('author/', views.add_author ,name='add_author'),
   
]
