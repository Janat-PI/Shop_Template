from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(150)(BaseView.as_view()), name='base'),
    path('products/<str:ct_model>/<str:slug>/', cache_page(250)(ProductDetailView.as_view()), name='product_detail'),
    path('category/<str:slug>/', cache_page(60)(CategoryDetailView.as_view()), name='category_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:ct_model>/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:ct_model>/<str:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-qty/<str:ct_model>/<str:slug>/', ChangeQTYView.as_view(), name='change_qty'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('make-order/', MakeOrderView.as_view(), name='make_order'),
    path('payed-online-order/', PayedOnlineOrderView.as_view(), name='make_order'),
]

