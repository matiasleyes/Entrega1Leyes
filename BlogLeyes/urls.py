from django.urls import path
from BlogLeyes import views

urlpatterns = [

    path('',views.inicio, name='Inicio'),
    path('inicio',views.inicio, name='Inicio'),

    #Login-----------
    path('login/',views.login_request, name="Login"),
    path('register/', views.register, name='Register'),
    
    #Writer----------
    path('writer/list',views.writerList.as_view(),name='writerList'),
    path(r'^(?P<pk>\d+)$',views.writerDetail.as_view(),name='writerDetail'),
    path(r'^nuevo$',views.writerMake.as_view(),name='writerNew'),
    path(r'^editar/(?P<pk>\d+)$',views.writerUpdate.as_view(),name='writerEdit'),
    path(r'^borrar/(?P<pk>\d+)$',views.writerDelete.as_view(),name='writerDelete'),

    #Owner----------
    path('owner/list',views.ownerList.as_view(),name='ownerList'),
    path(r'^(?P<pk>\d+)$',views.ownerDetail.as_view(),name='ownerDetail'),
    path(r'^nuevo$',views.ownerMake.as_view(),name='ownerNew'),
    path(r'^editar/(?P<pk>\d+)$',views.ownerUpdate.as_view(),name='ownerEdit'),
    path(r'^borrar/(?P<pk>\d+)$',views.ownerDelete.as_view(),name='ownerDelete'),

    #Themes----------
    path('themes/list',views.themesList.as_view(),name='themesList'),
    path(r'^(?P<pk>\d+)$',views.themesDetail.as_view(),name='themesDetail'),
    path(r'^nuevo$',views.themesMake.as_view(),name='themesNew'),
    path(r'^editar/(?P<pk>\d+)$',views.themesUpdate.as_view(),name='themesEdit'),
    path(r'^borrar/(?P<pk>\d+)$',views.themesDelete.as_view(),name='themesDelete'),

    
    path('articulo', views.articulo, name='Articulo'),
    path('donor/', views.donor, name='Donor'),
    path('topics/', views.topics, name='Topics'),
    path('busquedaEscritor/', views.busquedaEscritor, name="BusquedaEscritor"),
    path('buscar/', views.buscar, name='buscar'),
]