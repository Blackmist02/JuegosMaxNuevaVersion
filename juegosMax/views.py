from .models import Juego, Carrito, ItemCarrito, Imagen, Comentario
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from .form import *
import random
from django.template import RequestContext

# Create your views here.

def home(request):
    banner = Juego.objects.all().order_by('fecha_creacion')
    NovedadesGames = Juego.objects.all().order_by('fecha_creacion')[:3]
    return render(request, 'juegosMax/index.html', {'NovedadesGames': NovedadesGames, 'banner': banner})

def login_view(request):
    imagenes = Imagen.objects.all()
    imagen_aleatoria = random.choice(imagenes)
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('juegosMax/index.html')
    else:
        form = LoginForm()
        return render(request, 'juegosMax/login.html', {'form': form, 'imagen_aleatoria': imagen_aleatoria})

def logout_view(request):
    logout(request)
    return redirect('index')



def signup(request):
    imagenes = Imagen.objects.all()
    imagen_aleatoria = random.choice(imagenes)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Cambia 'home' por la URL a la que quieres redirigir tras registrarse
    else:
        form = SignUpForm()
    return render(request, 'juegosMax/signup.html', {'form': form, 'imagen_aleatoria': imagen_aleatoria})


def juego(request, juego_id=None):
    if juego_id is None:
        juego_id = request.session.get('last_game_id', None)
        if juego_id is None:
            return render(request, 'juegosMax/juego.html', {'juego': None})
    juego = Juego.objects.get(pk=juego_id)
    comentarios = Comentario.objects.filter(juego=juego).order_by('-fecha_creacion')
    return render(request, 'juegosMax/juego.html', {'juego': juego, 'comentarios': comentarios})


@login_required(login_url='login')
def agregar_comentario(request, juego_id):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            juego = get_object_or_404(Juego, pk=juego_id)
            comentario = Comentario(
                juego=juego,
                usuario=request.user.username,
                comentario=form.cleaned_data['comentario'],
            )
            comentario.save()
            return redirect('juego', juego_id=juego_id)
    else:
        juego = Juego.objects.get(pk=juego_id)
        form = ComentarioForm(initial={'juego_id': juego_id})
    return render(request, 'juego.html', {'juego': juego, 'form': form})

def faq(request):
    return render(request, 'juegosMax/faq.html')

@login_required(login_url='login')
def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'juegosMax/contacts.html', {'form': form})

def errorPage(request):
    return render(request, 'juegosMax/404.html')

def consolaNinSwitch(request):
    juegosTipoConsola = Juego.objects.filter(plataforma__icontains='Nintendo Switch')
    NovedadesGames = juegosTipoConsola.order_by('fecha_creacion')[:3]
    return render(request, 'juegosMax/consola_Nintendo_Switch.html', {'NovedadesGames': NovedadesGames, 'juegosTipoConsola': juegosTipoConsola})

def consolaPs5(request):
    juegosTipoConsola = Juego.objects.filter(plataforma__icontains='PS5')
    NovedadesGames = juegosTipoConsola.order_by('-fecha_creacion')[:3]
    return render(request, 'juegosMax/consola_PlayStation_5.html',{'NovedadesGames': NovedadesGames, 'juegosTipoConsola': juegosTipoConsola})

def consolaXboxSeries(request):
    juegosTipoConsola = Juego.objects.filter(plataforma__icontains='Xbox Series X/S')
    NovedadesGames = juegosTipoConsola.order_by('fecha_creacion')[:3]
    return render(request, 'juegosMax/consola_Xbox_Series.html', {'NovedadesGames': NovedadesGames, 'juegosTipoConsola': juegosTipoConsola})

@login_required
def indexLogeado(request):
    banner = Juego.objects.all().order_by('-fecha_creacion')
    NovedadesGames = Juego.objects.all().order_by('-fecha_creacion')[:3]
    return render(request, 'juegosMax/index.html', {'NovedadesGames': NovedadesGames, 'banner': banner})


@login_required(login_url='login')
def agregar_Al_Carrito(request, product_id):
    producto = get_object_or_404(Juego, id=product_id)
    carrito, creado = Carrito.objects.get_or_create(user=request.user)
    carrito_item, creado = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)

    if not creado:
        carrito_item.cantidad += 1
    carrito_item.save()
    return redirect('view_carrito')


@login_required(login_url='login')
def view_carrito(request):
    carrito, creado = Carrito.objects.get_or_create(user=request.user)
    items = carrito.items.all()
    total = sum(item.total_price() for item in items)
    return render(request, 'juegosMax/view_cart.html', {'items': items, 'total': total})


@login_required(login_url='login')
def actualizar_carrito(request, product_id):
    producto = get_object_or_404(Juego, id=product_id)
    carrito = get_object_or_404(Carrito, user=request.user)
    item_carrito = get_object_or_404(ItemCarrito, carrito=carrito, producto=producto)

    if request.method == 'POST':
        cantidad = int(request.POST.get('quantity'))
        if cantidad > 0:
            item_carrito.cantidad = cantidad
            item_carrito.save()
        else:
            item_carrito.delete()
    return redirect('view_carrito')

@login_required(login_url='login')
def view_pago(request):
    imagenes = Imagen.objects.all()
    imagen_aleatoria = random.choice(imagenes)
    carrito, creado = Carrito.objects.get_or_create(user=request.user)
    items = carrito.items.all()
    total = sum(item.total_price() for item in items)
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            # Procesar el pago
            # Limpiar el carrito
            carrito.items.all().delete()
            numero_tarjeta = form.cleaned_data['numero_tarjeta']
            fecha_expiracion  = form.cleaned_data['fecha_expiracion']
            cvv = form.cleaned_data['cvv']
            return render(request, 'juegosMax/pago_realizado.html',{'imagen_aleatoria': imagen_aleatoria})
    else:
        form = PagoForm()
    return render(request, 'juegosMax/pago.html', {'items': items, 'total': total, 'form': form, 'imagen_aleatoria': imagen_aleatoria})


from django.contrib.auth.decorators import login_required, user_passes_test

def admin_check(user):
    return user.is_superuser

@user_passes_test(admin_check)
@login_required()
def agregar_Juego(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST, request.FILES)
        if form.is_valid():
            juego = form.save()
            return redirect('juego', juego_id=juego.id)
    return render(request, 'juegosMax/agregar_Juego.html', {'form': JuegoForm()})


@user_passes_test(admin_check)
@login_required()
def modificar_juego(request, juego_id):
    juego = get_object_or_404(Juego, pk=juego_id)

    ImagenFormSet = inlineformset_factory(Juego, Imagen, form=ImagenFormModificacion, extra=0, can_delete=True)

    if request.method == 'POST':
        juego_form = JuegoFormModificacion(request.POST, instance=juego)
        imagen_formset = ImagenFormSet(request.POST, request.FILES, instance=juego, prefix='imagenes')
        trailer_form = TrailerFormModificacion(request.POST,
                                               instance=juego.trailers.first() if juego.trailers.exists() else None)

        if juego_form.is_valid() and imagen_formset.is_valid() and trailer_form.is_valid():
            juego_form.save()
            imagen_formset.save()

            trailer = trailer_form.save(commit=False)
            trailer.juego = juego
            trailer.save()

            return redirect('juego', juego_id=juego.id)
    else:
        juego_form = JuegoFormModificacion(instance=juego)
        imagen_formset = ImagenFormSet(instance=juego, prefix='imagenes')
        trailer_form = TrailerFormModificacion(instance=juego.trailers.first() if juego.trailers.exists() else None)

    return render(request, 'juegosMax/modificar_juego.html', {
        'juego_form': juego_form,
        'imagen_formset': imagen_formset,
        'trailer_form': trailer_form,
        'juego': juego,
    })


@user_passes_test(admin_check)
@login_required()
def eliminar_juego(request, juego_id):
    juego = get_object_or_404(Juego, pk=juego_id)

    if request.method == 'POST':
        juego.delete()
        return redirect('index')

    return render(request, 'juegosMax/eliminar_juego.html', {'juego': juego})