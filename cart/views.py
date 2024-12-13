from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from shop.models import Perfume

@login_required(login_url='register')
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user).annotate(
        total_price=F('quantity') * F('perfume__price')
    )

    return render(request, 'cart.html', {'cart_items': cart_items})

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
