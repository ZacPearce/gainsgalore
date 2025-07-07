import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Payment
from workouts.models import WorkoutPlan
from users.models import CustomUser

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request, workout_id):
    workout = WorkoutPlan.objects.get(id=workout_id)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'gbp',
                'unit_amount': 999,  # price in pence (£9.99)
                'product_data': {
                    'name': workout.title,
                },
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8002/payments/success/',
        cancel_url='http://127.0.0.1:8002/payments/cancel/',
    )

    return redirect(session.url, code=303)

def payment_success(request):
    return render(request, 'payments/success.html')

def payment_cancel(request):
    return render(request, 'payments/cancel.html')
