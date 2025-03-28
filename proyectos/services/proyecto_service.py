from proyectos.models.proyecto import Proyecto 

def obtener_proyectos():
    return Proyecto.objects.all()

def obtener_proyecto(nombre):
    return Proyecto.objects.get(nombre=nombre)

def crear_proyecto(datos):
    return Proyecto.objects.create(**datos)

def actualizar_proyecto(proyecto, datos):
    for key, value in datos.items():
        setattr(proyecto, key, value)
    proyecto.save()
    return proyecto