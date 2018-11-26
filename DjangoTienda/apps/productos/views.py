from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from apps.productos.models import producto,categoria
from django.views.generic.list import ListView
from django.template import Context, loader
from django.views.generic.base import TemplateView
from apps.productos.formulario import ProductoForm,CategoriaForm
from django.db.models import F,Sum
from collections import Counter

	
def index(request): 
	return HttpResponse("Esta es la respuesta index")


def product(request):
	contexto = { 
		'productos': producto.objects.all(),'categorias': categoria.objects.all()
	}
	return render(request, 'productos/productos.html',contexto)

def home2(request):
	contexto = { 
		'productos': producto.objects.all(),'categorias': categoria.objects.all()
	}
	return render(request, 'productos/home.html',contexto)	
		

def categorias(request):
	contexto = { 
		'categorias': categoria.objects.all()
	}
	return render(request, 'productos/categorias.html',contexto)
	

	return render(request, 'productos/productos.html', contexto)
	

def addP(request):
	if request.method == 'POST':
		form=ProductoForm(request.POST) 
		if form.is_valid(): 
			form.save() 
		return redirect('product') 
	else: 
		form = ProductoForm() 

	
	return render(request,'productos/pForm.html')


def addC(request):
	if request.method == 'POST':
		form=CategoriaForm(request.POST) 
		if form.is_valid():
			form.save() 
		return redirect('categorias') 
	else: 
		form = CategoriaForm()

	
	return render(request,'productos/cForm.html',{'form': form})


def editP(request,idProducto): 

	instance = get_object_or_404(producto, id=idProducto)
	form = ProductoForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
		return redirect('product')

	return render(request, 'productos/editP.html', {'form': form}) 


def eliminarProducto(request,idProducto):
	Producto=producto.objects.get(id=idProducto)
	Producto.delete()
	return redirect('product')



def editC(request,idCategoria): 

	instance = get_object_or_404(categoria, id=idCategoria)
	form = CategoriaForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
		return redirect('categorias')

	return render(request, 'productos/editC.html', {'form': form}) 


def eliminarCategoria(request,idCategoria):
	Categoria=categoria.objects.get(id=idCategoria)
	Categoria.delete()
	return redirect('categorias')


def x(request):
	contexto = { 
		'productos': producto.objects.exclude(numeroExistencias=0),'categorias': categoria.objects.all()
	}
	return render(request, 'productos/cart.html',contexto)


def agregarCarrito(request,idProducto):

	items=request.session.get('ids')
	if  items== None:
		items=[idProducto] 
	else:
		items.append(idProducto)
	
	request.session['ids']=items
	return redirect('shopCart')




def cart(request):
	items=request.session.get('ids')
	"""contextoD=0
	for x in range(0,len(items)):
		contextoD +=(producto.objects.filter(id=items[x]))"""
	contexto = { 
		'productos': producto.objects.filter(id__in=items)
	}
	total=0
	total=(producto.objects.filter(id__in=items).aggregate(Sum('costo')))
	contexto['total']=total

	return render(request, 'productos/cart.html',contexto)


	
def confirmar(request):
	items=request.session.get('ids')
	contexto=  producto.objects.filter(id__in=items)
	total=0
	for x in range(0,len(contexto)):
		contexto[x].numeroExistencias=contexto[x].numeroExistencias-1
		contexto[x].save()
	
	request.session.pop('ids')
		
	return redirect('cart')

