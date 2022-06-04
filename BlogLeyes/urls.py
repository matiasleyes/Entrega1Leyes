from django.urls import path
from BlogLeyes import views

urlpatterns = [
    path('writer/', views.writer, name='Writer'),
    path('articulo', views.articulo, name='Articulo'),
    path('owner/', views.owner, name='Owner'),
    path('inicio/',views.inicio, name='Inicio'),
    path('donor/', views.donor, name='Donor'),
    path('themes/', views.themes, name='Theme'),
    path('topics/', views.topics, name='Topics'),
    path('',views.inicio, name='Inicio'),
]