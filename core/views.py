from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "core/index.html")

def productos(request):
    return render(request, "core/productos.html")
