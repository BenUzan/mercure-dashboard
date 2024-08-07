from django.urls import path

from apps.sales import views


urlpatterns = [
    path('daily-report', views.report, name='daily_report'),
    path('create-product', views.create_product, name='create_product'),
    path('create-order', views.create_order, name='create_order'),
    path('product-list', views.product_list, name='product_list'),
    path('update-product/<int:id>',
         views.update_product, name='update-product'),
    path('product-list/update-product/upr/<int:id>',
         views.update_product_record, name='upr'),
    path("delete-product/<int:id>",
         views.delete_product, name="delete_product")
]
