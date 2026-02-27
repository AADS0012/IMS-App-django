from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('product/create/', views.product_create_view, name='product_create'),
    path('product/', views.products_list_view, name='product_list'),
    path('product/update/<int:product_id>/', views.products_update_view, name='product_update'),
    path('product/delete/<int:product_id>/', views.product_delete_view, name='product_delete'),
]