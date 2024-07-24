from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('daily-report/', views.report, name='daily-report'),
    path('create-product/', views.create_product, name='cp'),
    path('create-order/', views.create_order, name='create_order'),
    path('product-list/', views.product_list, name='product-list'),
    path('product-list/up/<int:id>/', views.update_product, name='up'),
    path('product-list/up/upr/<int:id>/',
         views.update_product_record, name='upr'),
    path("product-list/dp/<int:id>/", views.delete_product, name="dp")

]
