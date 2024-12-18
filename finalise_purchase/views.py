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

    line_items = []
    for item in cart_items:
        line_items.append({
            'price_data': {
                'currency': 'gbp', 
                'product_data': {
                    'name': item.perfume
                },
                'unit_amount': int(item.perfume.price * 100),
            },
            'quantity': item.quantity,
        })

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url='http://127.0.0.1:8000/success/',
        cancel_url='http://127.0.0.1:8000/cancel/',
    )

    context = {
        'publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
        'session_id': session.id,
    }
    print(f"Stripe Session ID: {session.id}")

    return render(request, 'finalise_purchase/finalise_purchase.html', context)

def success(request):
    return render(request, 'success.html')

def cancel(request):
    return render(request, 'cancel.html')
