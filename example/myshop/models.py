from django.db import models
from django.utils.translation import ugettext_lazy as _

from polymorphic.manager import PolymorphicManager
from shop.models.productmodel import Product
from discount.models import DiscountBase


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=100)

    def __unicode__(self):
        return self.name


class BookManager(PolymorphicManager):
    """A dumb manager to test the behavior with poylmorphic"""
    def get_all(self):
        return self.all()


class Book(Product):
    isbn = models.CharField(max_length=255)
    short_description = models.CharField(_('Short description'), 
            max_length=100, blank=True)
    long_description = models.TextField(_('Long description'), blank=True)
    categories = models.ManyToManyField(Category, null=True, blank=True)

    objects = BookManager()


class BulkDiscount(DiscountBase):
    """
    Apply ``amount`` % of discount if there are at least ``num_items`` of
    product in cart.
    """
    amount = models.DecimalField(_('Amount'), max_digits=5, decimal_places=2)
    num_items = models.IntegerField(_('Minimum number of items'))

    def process_cart_item(self, cart_item):
        if (cart_item.quantity >= self.num_items and
            self.is_eligible_product(cart_item.product, cart_item.cart)):
            amount = (self.amount/100) * cart_item.line_subtotal
            to_append = (self.get_name(), amount)
            cart_item.extra_price_fields.append(to_append)

    class Meta:
        verbose_name = _('Bulk discount')
        verbose_name_plural = _('Bulk discounts')


# filter function
def category_product_filter(discount, queryset):
    """
    Allow discount type to be filtered by category.
    """
    if not discount.categories.count():
        return queryset
    ids = [c.id for c in discount.categories.all()]
    return queryset.filter(models.Q( Book___categories__id__in=ids))

DiscountBase.register_product_filter(category_product_filter)

#add categories field to BulkDiscount
DiscountBase.add_to_class('categories', 
        models.ManyToManyField(Category, 
            verbose_name=_('Categories'),
            blank=True,
            null=True,
            help_text=_('Limit discount to selected categories')
            ))


