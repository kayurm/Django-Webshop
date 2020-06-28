from django.urls import path

from apps.core.views import (
    index, category_list, category_detail, product_list, product_detail
)

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('categories/', category_list, name='category-list'),
    path('categories/<slug>/', category_detail, name='category-detail'),
    path('products/', product_list, name='product-list'),
    path('products/<slug_category>/<pk>/', product_detail, name='product-detail'),
]
