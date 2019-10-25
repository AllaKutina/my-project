from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from .models import Category, Product


class CategoriesList(ListView):
    model = Category


class CategoriesDetail(DetailView):
    model = Category
    template_name = 'catalog_detail.html'

class ProductsList(ListView):
    model = Product


class ProductsDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'


class MainPage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {
            'categories': Category.objects.all()
        }


class CatalogPage(TemplateView):
    template_name = 'catalog.html'

    def get_context_data(self, **kwargs):
        return {
            'products': Product.objects.all(),
        }