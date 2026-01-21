from django.shortcuts import get_object_or_404, render

from diplom_app.models import Product, Categories


def main_page(request):
    products = Product.objects.all()
    categories = Categories.objects.all()
    ctx = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'main_page.html', ctx)