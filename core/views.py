from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm, LoginForm, ProfileForm

# === TUS PÁGINAS SIMPLES ===
def home(request):
    return render(request, "home.html")

def reservar(request):
    return render(request, "reservar.html")

def tratamientos(request):
    return render(request, "tratamientos.html")

def conocenos(request):
    return render(request, "conocenos.html")


# === AUTENTICACIÓN Y PERFILES ===
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email'].lower()
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=email, email=email, password=password)
            user.is_active = False
            user.save()

            # crear link de activación
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_link = request.build_absolute_uri(
                reverse('core:activate', kwargs={'uidb64': uid, 'token': token})
            )
            subject = 'Activa tu cuenta'
            message = render_to_string('activation_email.html', {
                'user': user,
                'activation_link': activation_link,
            })
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

            messages.success(request, "Cuenta creada. Revisa tu correo para activarla.")
            return redirect('core:login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception:
        user = None
    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        if hasattr(user, 'profile'):
            user.profile.email_verified = True
            user.profile.save()
        messages.success(request, "Cuenta activada. Ahora puedes iniciar sesión.")
        return redirect('core:login')
    else:
        return render(request, 'activation_invalid.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email'].lower()
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('core:profile')
                else:
                    messages.error(request, "Cuenta no activada. Revisa tu correo.")
            else:
                messages.error(request, "Credenciales incorrectas.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('core:login')


@login_required
def profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado.")
            return redirect('core:profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile.html', {'form': form})
