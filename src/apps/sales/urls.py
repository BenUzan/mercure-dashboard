from django.urls import path

from apps.sales import views

# ! TEMPORAIRE
urlpatterns = [
    path('daily-report', views.report, name='daily_report'),
    path('delivery', views.delivery, name='delivery'),
    path('report-list', views.report_list, name='report-list'),
    path('report-details/<int:id>',
         views.report_details, name='report-details'),
    path('extra-report-details/<int:id>',
         views.extra_report_details, name='extra-report-details'),
    path('report-download/<int:id>', views.generate_report, name='report-download'),
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
