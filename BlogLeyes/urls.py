from django.urls import path
from BlogLeyes import views

urlpatterns = [
    #Login-----------
    path('login/',views.login_request, name="Login"),
    path('register/', views.register, name='Register'),
    
    
    path('writer/', views.writer, name='Writer'),
    path('articulo', views.articulo, name='articulo'),
    path('owner/', views.owner, name='Owner'),
    path('inicio/',views.inicio, name='Inicio'),
    path('donor/', views.donor, name='Donor'),
    path('themes/', views.themes, name='Theme'),
    path('topics/', views.topics, name='Topics'),
    path('',views.inicio, name='Inicio'),
    path('busquedaEscritor/', views.busquedaEscritor, name="BusquedaEscritor"),
    path('buscar/', views.buscar, name='buscar'),
    path('aboutus/', views.aboutus, name='Aboutus'),

]