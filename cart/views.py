from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F
from cart.models import CartItem
from shop.models import Perfume

def cart(request):
    if request.user.is_authenticated:
        # Fetch CartItems from the database for authenticated users
        cart_items = CartItem.objects.filter(user=request.user).annotate(
            total_price=F('quantity') * F('perfume__price')
        )
    else:
        # For unauthenticated users, pull the cart from the session
        session_cart = request.session.get('cart', {})
        cart_items = [
            {
                'name': item_data['name'],
                'size': item_data['size'],
                'price': item_data['price'],
                'quantity': item_data['quantity'],
                'image': item_data['image'],
                'total_price': item_data['price'] * item_data['quantity'],
            }
            for item_data in session_cart.values()
        ]

    return render(request, 'cart.html', {'cart_items': cart_items})




def add_to_cart(request, perfume_id):
    perfume = get_object_or_404(Perfume, id=perfume_id)
    size = request.POST.get('size')
    quantity = int(request.POST.get('quantity', 1))

    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            perfume=perfume,
            size=size
        )
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()
    else:
        cart = request.session.get('cart', {})
        item_id = f"{perfume_id}-{size}"
        if item_id in cart:
            cart[item_id]['quantity'] += quantity
        else:
            cart[item_id] = {
                'name': perfume.name,
                'size': size,
                'price': float(perfume.price),
                'quantity': quantity,
                'image': perfume.image.url,
            }
        request.session['cart'] = cart

    return redirect('cart')

