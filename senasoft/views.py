from django.shortcuts import render, redirect
from .models import Competidor
from .forms import CompetidorForm

def bienvenida(request):
    return render(request, 'senasoft/bienvenida.html')

def registro(request):
    if request.method == 'POST':
        form = CompetidorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('competidores')
    else:
        form = CompetidorForm()
    return render(request, 'senasoft/registro.html', {'form': form})

def competidores(request):
    lista = Competidor.objects.all()
    return render(request, 'senasoft/competidores.html', {'competidores': lista})