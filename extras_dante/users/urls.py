from django.urls import path
from .views import login_view, register_view, home_view, logout_view

urlpatterns = [
    path('', login_view, name='login'),  # Página de inicio predeterminada para login
    path('register/', register_view, name='register'),  # Formulario de registro
    path('home/', home_view, name='home'),  # Página principal después de iniciar sesión
    path('logout/', logout_view, name='logout'),  # Cerrar sesión
]
