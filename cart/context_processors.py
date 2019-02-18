"""Cart context processors module."""

from .cart import Cart


def cart(request):
    """Put cart variable in template context."""
    return {'cart': Cart(request)}
