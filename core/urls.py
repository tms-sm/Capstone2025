from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("reservar/", views.reservar, name="reservar"),
    path("tratamientos/", views.tratamientos, name="tratamientos"),
    path("conocenos/", views.conocenos, name="conocenos"),

    # Autenticación
    path("register/", views.register, name="register"),
    path("activate/<uidb64>/<token>/", views.activate, name="activate"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),
]
