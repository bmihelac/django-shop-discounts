from shop.cart.cart_modifiers_base import BaseCartModifier

from models import DiscountBase


class DiscountCartModifier(BaseCartModifier):

    def get_active_discounts(self, cart):
        """
        Returns active discounts for cart object.
        """
        cartdiscountcode_set = cart.cartdiscountcode_set.all()
        if cartdiscountcode_set:
            code = cartdiscountcode_set[0].code
        else:
            code = ''
        return DiscountBase.objects.active(code=code)

    def add_extra_cart_item_price_field(self, cart_item):
        for discount in self.get_active_discounts(cart_item.cart):
            discount.process_cart_item(cart_item)
        return cart_item

    def add_extra_cart_price_field(self, cart):
        for discount in self.get_active_discounts(cart):
            discount.process_cart(cart)
        return cart
