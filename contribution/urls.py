from django.urls import path
from . import views

urlpatterns = [
    path('', views.contribution_list, name='contribution_list'),
    path('contribution/<int:pk>/', views.contribution_detail, name='contribution_detail')
]
