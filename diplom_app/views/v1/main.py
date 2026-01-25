from django.shortcuts import render

from diplom_app.models import Product, Category


def main_page(request):
    products = Product.objects.all().select_related('category', 'business_turi')
    categories = Category.objects.all()
    ctx = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'main_page.html', ctx)