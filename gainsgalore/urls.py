from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("""
        <h1>Welcome to Gains Galore 💪🏾</h1>
        <p>
            <a href='/users/login/'>Login</a> |
            <a href='/users/register/'>Register</a>
        </p>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('payments/', include('payments.urls')),
    path('', home_view, name='home'),
]
