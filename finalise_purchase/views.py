import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from cart.models import CartItem

stripe.api_key = settings.STRIPE_SECRET_KEY

def finalise_purchase(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items.exists():
        return redirect('cart')

    line_items = [
        {
            'price_data': {
                'currency': 'gbp',
                'product_data': {
                    'name': item.perfume.name,
                },
                'unit_amount': int(item.perfume.price * 100),
            },
            'quantity': item.quantity,
        }
        for item in cart_items
    ]

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=request.build_absolute_uri('/finalise_purchase/success/'),
        cancel_url=request.build_absolute_uri('/finalise_purchase/cancel/'),
    )

    return redirect(session.url, code=303)

def success(request):
    return render(request, 'finalise_purchase/success.html')

def cancel(request):
    return render(request, 'finalise_purchase/cancel.html')
