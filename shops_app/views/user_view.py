from django.shortcuts import render, redirect, get_object_or_404
from shops_app.models import Shop, Product
from shops_app.services.services import get_basket
from django.http import JsonResponse

def view_shop_page(request, shop_slug):
    shop = get_object_or_404(Shop, slug=shop_slug)
    products = shop.products.all()
    cart_data = get_basket(request)
    ctx = {
        "shop": shop,
        "product": products,
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



def add_to_basket(request, shop_slug, product_id):
    shop = get_object_or_404(Shop, slug=shop_slug)
    basket = request.session.get('basket', {})
    p_id = str(product_id)
    if p_id in basket:
        basket[p_id] += 1
    else:
        basket[p_id] = 1

    request.session['basket'] = basket
    request.session.modified = True

    return JsonResponse({'status': 'ok', 'cart_count': len(basket)})




































