from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from juegosMax.models import Imagen, Trailer, Juego


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Correo Electronico', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Nombre de Usuario', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

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

        from_email = 'TuEmail@example.com'
        recipient_list = ['recipient_email@example.com']

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


class JuegoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}))
    descripcionCorta = forms.CharField(label='Descripción corta', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}))
    fecha_lanzamiento = forms.DateField(label='Fecha de lanzamiento', widget=forms.DateInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}))
    desarrollador = forms.CharField(label='Desarrollador', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}))
    genero = forms.CharField(label='Género', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}))
    plataforma = forms.CharField(label='Plataforma', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}))
    clasificacion = forms.CharField(label='Clasificación', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}))
    idioma = forms.CharField(label='Idioma', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}))
    requisitos = forms.CharField(label='Requisitos', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}))
    stock = forms.IntegerField(label='Stock', widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}))
    available = forms.BooleanField(label='Disponible', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'background-color: #40010D; color: white;'}))
    precio = forms.IntegerField(label='Precio', widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}))
    descripcionExtensa = forms.CharField(label='Descripción', widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}))

    imagen1 = forms.ImageField(label='Imagen 1', widget=forms.FileInput(attrs={'class': 'form-control'}))
    imagen2 = forms.ImageField(label='Imagen 2', required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    imagen3 = forms.ImageField(label='Imagen 3', required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    imagen4 = forms.ImageField(label='Imagen 4', required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    video_url = forms.URLField(label='URL del video', widget=forms.URLInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}))
    img_url = forms.CharField(label='URL de la miniatura del video', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}))

    def save(self):
        juego = Juego(
            nombre=self.cleaned_data['nombre'],
            descripcion=self.cleaned_data['descripcionCorta'],
            fecha_lanzamiento=self.cleaned_data['fecha_lanzamiento'],
            desarrolladora=self.cleaned_data['desarrollador'],
            genero=self.cleaned_data['genero'],
            plataforma=self.cleaned_data['plataforma'],
            clasificacion=self.cleaned_data['clasificacion'],
            idioma=self.cleaned_data['idioma'],
            requisitos=self.cleaned_data['requisitos'],
            stock=self.cleaned_data['stock'],
            available=self.cleaned_data['available'],
            precio=self.cleaned_data['precio'],
            descripcionExtensa=self.cleaned_data['descripcionExtensa']
        )
        juego.save()


        # Crear imágenes asociadas
        imagenes = [
            self.cleaned_data.get('imagen1'),
            self.cleaned_data.get('imagen2'),
            self.cleaned_data.get('imagen3'),
            self.cleaned_data.get('imagen4')
        ]

        for i, imagen in enumerate(imagenes):
            if imagen:
                Imagen.objects.create(juego=juego, imagen=imagen, orden=i)

        # Crear trailer asociado
        Trailer.objects.create(
            juego=juego,
            video_url=self.cleaned_data['video_url'],
            img_url=self.cleaned_data['img_url']
        )

        return juego



class JuegoFormModificacion(forms.ModelForm):
    class Meta:
        model = Juego
        fields = [
            'nombre', 'descripcion', 'fecha_lanzamiento', 'desarrolladora',
            'genero', 'plataforma', 'clasificacion', 'idioma',
            'requisitos', 'stock', 'available', 'precio', 'descripcionExtensa'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}),
            'fecha_lanzamiento': forms.DateInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}),
            'desarrolladora': forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}),
            'genero': forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}),
            'plataforma': forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}),
            'clasificacion': forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}),
            'idioma': forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}),
            'requisitos': forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}),
            'available': forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'background-color: #40010D; color: white;'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}),
            'descripcionExtensa': forms.Textarea(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}),
        }


class ImagenFormModificacion(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = ['imagen', 'orden']
        widgets = {
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'orden': forms.HiddenInput(),
        }


class TrailerFormModificacion(forms.ModelForm):
    class Meta:
        model = Trailer
        fields = ['video_url', 'img_url']
        widgets = {
            'video_url': forms.URLInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}),
            'img_url': forms.TextInput(attrs={'class': 'form-control', 'style': 'background-color: #40010D; color: white;'}),
        }