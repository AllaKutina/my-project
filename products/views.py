from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from .models import Category, Product
from django.core.paginator import Paginator


class CategoriesList(ListView):
    model = Category


class CategoriesDetail(DetailView):
    model = Category
    template_name = 'catalog_detail.html'

    def get_context_data(self, **kwargs):
       data = super().get_context_data(**kwargs)
       products = Product.objects.filter(category=data['object'])
       paginator = Paginator(products, 3)
       page = self.request.GET.get('page')
       data['products'] = paginator.get_page(page)

       return data


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


class CatalogPage(ListView):
    model = Product
    template_name = 'catalog.html'
    paginate_by = 3
    page_kwarg = 'page'