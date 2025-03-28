from django.shortcuts import render, get_object_or_404, redirect
from proyectos.models.proyecto import Proyecto
from proyectos.services.proyecto_service import obtener_proyectos, obtener_proyecto, crear_proyecto, actualizar_proyecto
from proyectos.forms.proyecto_form import ProyectoForm

def listar_proyectos(request):
    proyectos = obtener_proyectos()
    return render(request, 'proyectos/listar.html', {'proyectos': proyectos})

def registrar_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            crear_proyecto(form.cleaned_data)
            return redirect('listar_proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'proyectos/registrar.html', {'form': form})

def editar_proyecto(request, nombre):
   proyecto = get_object_or_404(Proyecto, nombre=nombre)
   if request.method == 'POST':
       form = ProyectoForm(request.POST, instance=proyecto)
       if form.is_valid():
           actualizar_proyecto(proyecto, form.cleaned_data)
           return redirect('listar_proyectos')
   else:
       form = ProyectoForm(instance=proyecto)
   return render(request, 'proyectos/editar.html', {'form': form})

