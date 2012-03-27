from django.db import models
from django.utils.translation import ugettext_lazy as _


class PercentDiscountMixin(models.Model):
    """
    Apply ``amount`` percent discount to whole cart.
    """
    amount = models.DecimalField(_('Amount'), max_digits=5, decimal_places=2)

    def get_extra_cart_price_field(self, cart):
        amount = (self.amount/100) * cart.subtotal_price
        return (self.get_name(), amount,)

    class Meta:
        abstract = True


class CartItemPercentDiscountMixin(models.Model):
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
        abstract = True


class CartItemAbsoluteDiscountMixin(models.Model):
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
        abstract = True
