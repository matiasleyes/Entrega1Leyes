from django.urls import path
from BlogLeyes import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('',views.inicio, name='Inicio'),
    path('inicio/',views.inicio, name='Inicio'),

    #Login----------------------------------------------------------------------------
    path('login/',views.login_request, name="Login"),
    path('register/', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='BlogLeyes/logout.html'), name = "Logout"),
    path('editarPerfil', views.editarPerfil, name = "editarPerfil"),
    #Writer----------------------------------------------------------------------------
    path('writer/list',views.writerList.as_view(),name='writerList'),
    path('writer/<pk>',views.writerDetail.as_view(),name='writerDetail'),
    path('writer/writerNew/',views.writerMake.as_view(),name='writerNew'),
    path('writer/edit/<pk>',views.writerUpdate.as_view(),name='writerEdit'),
    path('writer/delete/<pk>',views.writerDelete.as_view(),name='writerDelete'),

    #Owner----------------------------------------------------------------------------
    path('owner/list',views.ownerList.as_view(), name='ownerList'),
    path('owner/<pk>',views.ownerDetail.as_view(),name='ownerDetail'),
    path('owner/ownerNew/',views.ownerMake.as_view(),name='ownerNew'),
    path('owner/edit/<pk>',views.ownerUpdate.as_view(),name='ownerEdit'),
    path('owner/delete/<pk>',views.ownerDelete.as_view(),name='ownerDelete'),

    #Themes----------------------------------------------------------------------------
    path('themes/list', views.themesList.as_view(),name='themesList'),
    path('themes/<pk>', views.themesDetail.as_view(),name='themesDetail'),
    path('themes/themesNew/',views.themesMake.as_view(),name='themesNew'),
    path('themes/edit/<pk>',views.themesUpdate.as_view(),name='themesEdit'),
    path('themes/delete/<pk>',views.themesDelete.as_view(),name='themesDelete'),
    
    #Donor----------------------------------------------------------------------------
    path('donor/list', views.donorList.as_view(), name='donorList'),
    path('donor/<pk>', views.donorDetail.as_view(),name='donorDetail'),
    path('donor/donorNew/',views.donorMake.as_view(),name='donorNew'),
    path('donor/edit/<pk>',views.donorUpdate.as_view(),name='donorEdit'),
    path('donor/delete/<pk>',views.donorDelete.as_view(),name='donorDelete'),

    #Articulo----------------------------------------------------------------------------
    path('articulo/list',views.articuloList.as_view(),name='articuloList'),
    path('articulo/<pk>',views.articuloDetail.as_view(),name='articuloDetail'),
    path('articulo/articuloNew/',views.articuloMake.as_view(),name='articuloNew'),
    path('articulo/edit/<pk>',views.articuloUpdate.as_view(),name='articuloEdit'),
    path('articulo/delete/<pk>',views.articuloDelete.as_view(),name='articuloDelete'),

    #BUSQUEDA------------------------------------------------------------------------------
    path('busquedaEscritor/', views.busquedaEscritor, name="BusquedaEscritor"),
    path('buscar/', views.buscar, name='buscar'),

    #ABOUT US----------------------------------------------------------------------------
    path('aboutus/', views.aboutus, name='Aboutus'),

]