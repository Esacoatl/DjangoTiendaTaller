"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from apps.productos.views import index,product,addP,addC,categorias,editP,eliminarProducto,editC,eliminarCategoria,x,agregarCarrito,cart,confirmar,home2
from django.views.generic import TemplateView

app_name='productos'
urlpatterns = [
    path('home/', home2, name='home'),
    path('admin/', admin.site.urls),
    path('productos/',product,name="product"),
    path('', home2, name="home2"),
    path('addToCart/<idProducto>', agregarCarrito, name="agregarCarrito"),
    path('cart/', cart, name="shopCart"),
    path('confirmar/', confirmar, name="confirmar"),
    path('categorias/',categorias,name="categorias"),
    path('addP/',addP,name="addP"),
    path('addC/',addC,name="addC"),
    path('editP/<idProducto>',editP,name="editP"),
    path('deleteP/<idProducto>',eliminarProducto,name="eliminarProducto"),
    path('editC/<idCategoria>',editC,name="editC"),
    path('deleteC/<idCategoria>',eliminarCategoria,name="deleteC"),
    path('sell/',x,name="venta"),




    

]
