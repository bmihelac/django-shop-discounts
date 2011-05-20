from django.db import models
from django.utils.translation import ugettext_lazy as _

from polymorphic.manager import PolymorphicManager
from shop.models.productmodel import Product


class BookManager(PolymorphicManager):
    """A dumb manager to test the behavior with poylmorphic"""
    def get_all(self):
        return self.all()
    
class Book(Product):
    isbn = models.CharField(max_length=255)
    short_description = models.CharField(_('Short description'), 
            max_length=100, blank=True)
    long_description = models.TextField(_('Long description'), blank=True)
    
    objects = BookManager()

