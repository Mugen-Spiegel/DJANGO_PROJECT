from django.urls import path

from . import views



urlpatterns = [
    path('/', views.store),
    # path('products/', views.year_archive),
    # path('products/', views.year_archive),
    # path('products/<int:product_id>/', views.year_archive),
    # path('products/<int:product_id>/inventory/', views.year_archive),
]