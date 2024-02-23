from django.urls import path 
from . import views # importing all of our views

urlpatterns = [
    path('', views.post_list, name='post_list')
]