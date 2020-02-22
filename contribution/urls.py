from django.urls import path
from . import views

urlpatterns = [
    path('', views.contribution_list, name='contribution_list'),
    path('contribution/<int:pk>/', views.contribution_detail, name='contribution_detail'),
    path('contribution/new/', views.contribution_new, name='contribution_new'),
    path('contribution/<int:pk>/edit/', views.contribution_edit, name='contribution_edit'),
]
