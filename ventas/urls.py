from django.urls import path
from .views import OportunidadesAbm

urlpatterns = [
    path('oportunidades/', OportunidadesAbm.as_view(), name='oportunidades'),  # Ruta para detalles
]