from django.urls import path

from apps.stock import views

from apps.sales.views import product_list

urlpatterns = [
    path('stock-product-list', views.stock_product_list, name='stock_product_list'),
    path('stock-product-mgmt/<int:id>',
         views.stock_product_mgmt, name='stock-product-mgmt'),
]
