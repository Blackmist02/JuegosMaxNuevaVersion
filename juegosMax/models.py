from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from django.contrib.auth.models import User
# Create your models here.

class Juego(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    fecha_lanzamiento = models.DateField()
    desarrolladora = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    plataforma = models.CharField(max_length=50)
    clasificacion = models.CharField(max_length=50)
    idioma = models.CharField(max_length=50)
    requisitos = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    stock = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    precio = models.PositiveIntegerField(default=0)
    descripcionExtensa = models.CharField(max_length=1000)

    def __str__(self):
        return self.nombre

    @property
    def primera_imagen(self):
        return self.imagenes.all().first()

    @property
    def segunda_imagen(self):
        return self.imagenes.all()[1] if self.imagenes.count() > 1 else None

    @property
    def tercera_imagen(self):
        return self.imagenes.all()[2] if self.imagenes.count() > 2 else None

    @property
    def cuarta_imagen(self):
        return self.imagenes.all()[3] if self.imagenes.count() > 3 else None


    @property
    def trailer(self):
        return self.trailers.first()

class Imagen(models.Model):
    juego = models.ForeignKey(Juego, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='portadas/')
    orden = models.PositiveIntegerField(editable=False, db_index=True)

    def __str__(self):
        return f"Imagen de {self.juego.nombre}"

    def save(self, *args, **kwargs):
        if self._state.adding:
            last_order = Imagen.objects.filter(juego=self.juego).aggregate(models.Max('orden'))['orden__max']
            self.orden = 1 if last_order is None else last_order + 1
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['orden']


class Trailer(models.Model):
    juego = models.ForeignKey(Juego, related_name='trailers', on_delete=models.CASCADE)
    video_url = models.URLField(default='')  # Campo para la URL del video
    img_url = models.URLField(default='')  # Campo para la URL de la imagen del video

    def __str__(self):
        return self.video_url

class Comentario(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=50)
    comentario = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comentario


class Carrito(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Carrito de {self.user.username}"


class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Juego, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} de {self.producto.nombre}"

    def total_price(self):
        return self.cantidad * self.producto.precio
