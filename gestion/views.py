from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Libro, Prestamo

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'gestion/lista_libros.html', {'libros': libros})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect('lista_libros')
    else:
        form = UserCreationForm()
    return render(request, 'gestion/register.html', {'form': form})

def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)

    if request.method == 'POST' and libro.disponible:
        Prestamo.objects.create(
            usuario=request.user,
            libro=libro
        )
        libro.disponible = False
        libro.save()
        return redirect('lista_libros')

    return render(request, 'gestion/detalle_libro.html', {'libro': libro})
