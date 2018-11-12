from django.urls import path
from .views import (
    PerfilView,
    MeusPedidos
)

urlpatterns = [
    path('', PerfilView.as_view(), name='perfil_home'),
    path('meus-pedidos/', MeusPedidos.as_view(), name='perfil_meus_pedidos'),

]
