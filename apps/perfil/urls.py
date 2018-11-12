from django.urls import path
from .views import (
    PerfilView,
)

urlpatterns = [
    path('', PerfilView.as_view(), name='perfil_home'),

]
