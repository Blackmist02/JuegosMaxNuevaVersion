from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.core.validators import RegexValidator
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class ContactForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    def send_email(self):
        subject = 'Nuevo mensaje de contacto'
        message = f"Nombre: {self.cleaned_data['nombre']}\n" \
                  f"Email: {self.cleaned_data['email']}\n" \
                  f"Mensaje: {self.cleaned_data['mensaje']}"

        from_email = 'TuEmail@example.com'  # Replace with your email address
        recipient_list = ['recipient_email@example.com']  # Replace with your recipient email address

        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False,
        )

class ComentarioForm(forms.Form):
    juego_id = forms.IntegerField(widget=forms.HiddenInput())
    comentario = forms.CharField(label='Comentario', widget=forms.Textarea(attrs={'class': 'form-control'}))


class PagoForm(forms.Form):
    numero_tarjeta = forms.CharField(label='Número de tarjeta', min_length=16, max_length=16, validators=[
            RegexValidator(
                regex='^\d{16}$',
                message='Ingrese solo números',
                code='invalid_numero_tarjeta'
            )
        ],widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;' }))
    fecha_expiracion = forms.CharField(label='Fecha de expiración (MM/YY)', min_length=5, max_length=5, validators=[
            RegexValidator(
                regex='^(0[1-9]|1[0-2])\/\d{2}$',
                message='La fecha de expiración debe estar en el formato MM/YY.',
                code='invalid_fecha_expiracion'
            )
        ],widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;' }))
    cvv = forms.CharField(label='CVV', min_length=3, max_length=4, validators=[
            RegexValidator(
                regex='^\d{3,4}$',
                message='El CVV debe contener entre 3 y 4 dígitos.',
                code='invalid_cvv'
            )
        ],widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;' }))