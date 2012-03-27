from discount import mixins
from discount.models import DiscountBase


class PercentDiscount(DiscountBase, mixins.PercentDiscountMixin):

    class Meta:
        app_label = 'discount'


class CartItemPercentDiscount(DiscountBase, mixins.CartItemPercentDiscountMixin):

    class Meta:
        app_label = 'discount'


class CartItemAbsoluteDiscount(DiscountBase, mixins.CartItemAbsoluteDiscountMixin):

    class Meta:
        app_label = 'discount'
