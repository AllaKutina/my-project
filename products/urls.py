from django.urls import path
from . import views
app_name="products"

urlpatterns = [
    path('catalog/<int:pk>', views.CategoriesDetail.as_view(), name="category"),
    path('product/<int:pk>', views.ProductsDetail.as_view(), name="product"),
]