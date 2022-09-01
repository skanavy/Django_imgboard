from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>/', views.index, name='thread')
]