from django.urls import path

from apps.stock import views

from apps.stock.views import get_items_ajax_view

urlpatterns = [
    path('stock-product-list', views.stock_product_list, name='stock_product_list'),
    path('create-stock', views.create_stock, name='create-stock'),
    path('stock-product-mgmt/<int:id>',
         views.stock_product_mgmt, name='stock-product-mgmt'),
       # AJAX view
    path(
        'get-items/',
        get_items_ajax_view,
        name='get_items'
    ),
]
