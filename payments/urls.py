from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<int:workout_id>/', views.create_checkout_session, name='checkout'),
    path('success/', views.payment_success, name='payment_success'),
    path('cancel/', views.payment_cancel, name='payment_cancel'),
]
