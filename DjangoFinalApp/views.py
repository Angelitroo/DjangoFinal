from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'lista_tareas.html', {'tareas': tareas})

def crear_tarea(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        estado = request.POST.get("estado", "por_realizar")

        if titulo and descripcion:
            Tarea.objects.create(titulo=titulo, descripcion=descripcion, estado=estado)
            return redirect('lista_tareas')

    return render(request, 'crear_tarea.html')

def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)

    if request.method == "POST":
        titulo = request.POST.get("titulo")
        if titulo:
            tarea.titulo = titulo
            tarea.save()
            return redirect("lista_tareas")

    return render(request, "editar_tarea.html", {"tarea": tarea})

def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)

    if request.method == "POST":
        tarea.delete()
        return redirect('lista_tareas')

    return render(request, 'eliminar_tarea.html', {'tarea': tarea})

def buscar_tareas(request):
    tareas = Tarea.objects.all()
    if 'estado' in request.GET:
        estado = request.GET['estado']
        tareas = tareas.filter(estado=estado)
    if 'fecha' in request.GET:
        fecha = request.GET['fecha']
        tareas = tareas.filter(fecha_creacion__date=fecha)
    return render(request, 'lista_tareas.html', {'tareas': tareas})