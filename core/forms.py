from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from .models import Profile

class RegistrationForm(forms.Form):
    email = forms.EmailField(label="Correo electrónico", max_length=255)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email).exists():
            raise ValidationError("Ya existe una cuenta con ese correo.")
        return email

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get("password1")
        p2 = cleaned.get("password2")
        if p1 and p2 and p1 != p2:
            raise ValidationError("Las contraseñas no coinciden.")
        # valida la contraseña con validators de Django
        if p1:
            try:
                password_validation.validate_password(p1)
            except ValidationError as e:
                raise ValidationError(e.messages)
        return cleaned

class LoginForm(forms.Form):
    email = forms.EmailField(label="Correo")
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'phone', 'avatar']