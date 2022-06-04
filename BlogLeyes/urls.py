from django.urls import path
from BlogLeyes import views

urlpatterns = [
    path('writer/', views.writer),
    path('articulo', views.articulo),
    path('owner/', views.owner),
    path('',views.inicio),
    path('donor/', views.donor),
    path('themes/', views.themes),
    path('topics/', views.topics),
]