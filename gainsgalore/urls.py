from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from workouts.models import WorkoutPlan

def home_view(request):
    if request.user.is_authenticated:
        workouts = WorkoutPlan.objects.all()
    else:
        workouts = WorkoutPlan.objects.filter(is_premium=False)

    return render(request, 'home.html', {'workouts': workouts})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('payments/', include('payments.urls')),
    path('', home_view, name='home'),
]
