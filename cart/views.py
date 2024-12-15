from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F, Sum
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from shop.models import Perfume

@login_required(login_url='register')
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user).annotate(
        calculated_total_price=F('quantity') * F('perfume__price')
    )
    
    total_cart_price = cart_items.aggregate(total=Sum(F('quantity') * F('perfume__price')))['total'] or 0.00

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_cart_price': total_cart_price})


@login_required
def add_to_cart(request, perfume_id):
    perfume = get_object_or_404(Perfume, id=perfume_id)
    size = request.POST.get('size')
    quantity = int(request.POST.get('quantity', 1))

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

    return redirect('cart')

def remove_from_cart(request, cart_item_id):
    # Ensure the user is authenticated
    if request.user.is_authenticated:
        # Remove the item from the database
        cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
        cart_item.delete()

    return redirect('cart')
