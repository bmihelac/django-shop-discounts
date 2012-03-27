from django.db import models
from django.utils.translation import ugettext_lazy as _

from discount.models import DiscountBase


class PercentDiscount(DiscountBase):
    """
    Apply ``amount`` percent discount to whole cart.
    """
    amount = models.DecimalField(_('Amount'), max_digits=5, decimal_places=2)

    def get_extra_cart_price_field(self, cart):
        amount = (self.amount/100) * cart.subtotal_price
        return (self.get_name(), amount,)

    class Meta:
        verbose_name = _('Cart percent discount')
        verbose_name_plural = _('Cart percent discounts')


class CartItemPercentDiscount(DiscountBase):
    """
    Apply ``amount`` percent discount to eligible_products in Cart.
    """
    amount = models.DecimalField(_('Amount'), max_digits=5, decimal_places=2)

    def get_extra_cart_item_price_field(self, cart_item):
        if self.is_eligible_product(cart_item.product, cart_item.cart):
            return (self.get_name(),
                    self.calculate_discount(cart_item.line_subtotal))

    def calculate_discount(self, price):
        return (self.amount/100) * price

    class Meta:
        verbose_name = _('Cart item percent discount')
        verbose_name_plural = _('Cart item percent discounts')


class CartItemAbsoluteDiscount(DiscountBase):
    """
    Apply ``amount`` discount to eligible_products in Cart.
    """
    amount = models.DecimalField(_('Amount'), max_digits=5, decimal_places=2)

    def get_extra_cart_item_price_field(self, cart_item):
        if self.is_eligible_product(cart_item.product, cart_item.cart):
            return (self.get_name(),
                    self.calculate_discount(cart_item.line_subtotal))

    def calculate_discount(self, price):
        return self.amount

    class Meta:
        verbose_name = _('Cart item absolute discount')
        verbose_name_plural = _('Cart item absolute discounts')
