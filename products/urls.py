from django.urls import path
from . import views
from .api.v1 import views as api_views
app_name="products"

urlpatterns = [
    path('catalog/<int:pk>', views.CategoriesDetail.as_view(), name="category"),
    path('product/<int:pk>', views.ProductsDetail.as_view(), name="product"),
    path('api/v1/category/', api_views.CategoryListCreateAPIView.as_view(), name="category_list"),
    path('api/v1/category/<int:pk>', api_views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v1/product/', api_views.ProductListCreateAPIView.as_view()),
    path('api/v1/product/<int:pk>', api_views.ProductRetrieveUpdateDestroyAPIView.as_view()),
]