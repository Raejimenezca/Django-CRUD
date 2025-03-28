from django.urls import path
from proyectos.views.proyecto_views import listar_proyectos, registrar_proyecto, editar_proyecto

urlpatterns = [
    path('', listar_proyectos, name='listar_proyectos'),
    path('registrar/', registrar_proyecto, name='registrar_proyecto'),
    path('editar/<str:nombre>/', editar_proyecto, name='editar_proyecto')
]