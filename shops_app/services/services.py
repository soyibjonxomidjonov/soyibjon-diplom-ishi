from shops_app.models import Product


def get_basket(request):
    cart = request.session.get('cart', {})

    cart_items = []
    total_price = 0

    for p_id, stock in cart.items():
        try:
            product = Product.objects.get(id=p_id)
            item_total = product.price * stock
            total_price += item_total
            cart_items.append(
                {
                    'product': product,
                    'stock': stock,
                    'item_total': item_total
                })
        except Product.DoesNotExist:
            continue

    return {'cart_items': cart_items, 'total_price': total_price}