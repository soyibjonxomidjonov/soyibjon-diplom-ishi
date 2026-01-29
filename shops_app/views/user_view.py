from django.shortcuts import render, redirect, get_object_or_404
from shops_app.models import Shop, Product
from shops_app.services.services import get_basket



def view_shop_page(request, shop_slug):
    shop = get_object_or_404(Shop, slug=shop_slug)
    products = shop.products.all()
    cart_data = get_basket(request)
    ctx = {
        "shop": shop,
        "products": products,
    }
    ctx.update(cart_data)
    return render(request, 'user/user_main.html', ctx)


def view_product_page(request, shop_slug, product_id):
    shop = get_object_or_404(Shop, slug=shop_slug)
    product = Product.objects.get(id=product_id, shop=shop)
    cart_data = get_basket(request)
    ctx = {
        "shop": shop,
        "product": product
    }
    ctx.update(cart_data)
    return render(request, 'user/user_product.html', ctx)







































