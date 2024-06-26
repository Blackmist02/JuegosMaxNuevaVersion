"""
URL configuration for JuegosMaxNuevaVersion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from juegosMax import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'juegosMax'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name="index"),
    path('juego/<int:juego_id>/', views.juego, name="juego"),
    path('juego/', views.juego, name="juego"),
    path('faq/', views.faq, name="faq"),
    path('contacto/', views.contacto, name="contacto"),
    path('404/', views.errorPage, name="404"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name='signup'),
    path('Nintendo_Switch/', views.consolaNinSwitch, name='Nintendo_Switch'),
    path('PS5/', views.consolaPs5, name='PS5'),
    path('Xbox_Series_X_S/', views.consolaXboxSeries, name='Xbox_Series_X'),
    path('login/juegosMax/index.html', views.indexLogeado, name='juegos_max_index'),
    path('agregar_Al_Carrito/<int:product_id>/', views.agregar_Al_Carrito, name='agregar_Al_Carrito'),
    path('view_carrito/', views.view_carrito, name='view_carrito'),
    path('actualizar_carrito/<int:product_id>/', views.actualizar_carrito, name='actualizar_carrito'),
    path('agregar_comentario/<int:juego_id>/', views.agregar_comentario, name='agregar_comentario'),
    path('pago/', views.view_pago, name='pago'),
    path('agregar_Juego',views.agregar_Juego, name='AgregarJuego'),
    path('juego/<int:juego_id>/modificar/', views.modificar_juego, name='modificar_juego'),
    path('juegos/eliminar/<int:juego_id>/', views.eliminar_juego, name='eliminar_juego'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
