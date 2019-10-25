from django.template import Library, loader
from products.models import Category

register = Library()


@register.simple_tag(takes_context=True)
def categories(context):
    request = context.get('request')
    return loader.render_to_string('products/main-menu.html', {
        'categories': Category.objects.all(),
    }, request=request)