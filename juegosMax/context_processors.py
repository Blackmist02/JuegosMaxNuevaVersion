# cart/context_processors.py
from .models import Carrito

def cart_context_processor(request):
    if request.user.is_authenticated:
        carrito, creado = Carrito.objects.get_or_create(user=request.user)
        items_carrito = carrito.items.all()
        carrito_Total = sum(item.total_price() for item in items_carrito)
        return {
            'items_carrito': items_carrito,
            'carrito_Total': carrito_Total,
            'items_carrito_contador': items_carrito.count()
        }
    else:
        return {
            'items_carrito': [],
            'carrito_Total': 0,
            'items_carrito_contador': 0
        }