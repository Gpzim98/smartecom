from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "wish/index.html"


class CategoriaView(TemplateView):
    template_name = "wish/categories.html"


class ProdutoView(TemplateView):
    template_name = "wish/product.html"


class CarrinhoView(TemplateView):
    template_name = "wish/cart.html"
