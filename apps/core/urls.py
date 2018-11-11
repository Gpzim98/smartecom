from django.urls import path
from .views import (
    HomeView,
    CategoriaView,
    ProdutoView,
    CarrinhoView,
    CheckoutView
)

urlpatterns = [
    path('', HomeView.as_view(), name='core_home'),
    path('categoria', CategoriaView.as_view(), name='core_categoria'),
    path('produto', ProdutoView.as_view(), name='core_produto'),
    path('carrinho', CarrinhoView.as_view(), name='core_carrinho'),
    path('chckout', CheckoutView.as_view(), name='core_checkout'),
]
