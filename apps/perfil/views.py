from django.views.generic import TemplateView


class PerfilView(TemplateView):
    template_name = "wish/perfil.html"


class MeusPedidos(TemplateView):
    template_name = "wish/meus_pedidos.html"
