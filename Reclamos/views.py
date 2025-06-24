from django.shortcuts import render, redirect
from .forms import ReclamoForm

def registrar_reclamo(request):
    if request.method == 'POST':
        form = ReclamoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Reclamos/exito.html')
    else:
        form = ReclamoForm()
    return render(request, 'Reclamos/formulario.html', {'form': form})

def landing_page(request):
    return render(request, 'Reclamos/index.html')

