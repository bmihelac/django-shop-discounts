================
Custom discounts
================

Adding custom discount types is easy and can be achived with subclassing
polymorphic model ``discount.models.DiscountBase``.

Custom discount types can add fields and override following methods:

* ``get_products`` to filter initial product queryset discount operates on.
  Overriding this allows to say that discount should be applied only to some
  categories, for example.

  See also :doc:`filters`

* ``get_extra_cart_item_price_field`` - for adding extra cart item price field
  to cart items containing eligible products

* ``get_extra_cart_price_field`` - for adding extra cart price field to cart

Design considerations
---------------------

While django-shop-discount app comes with few bundled discount types, it does
not asume how specific shop is organized or how discount logic should work.

Typical discounts organization can set base constrains in base discount class
and specifing constrains in subclasses.

For example::

    class SiteBaseDiscount(DiscountBase):
        categories = models.ManyToManyField('myshop.Category',
                help_text=_('Limit discount to selected categories')

        def get_products():
            qs = super(SiteBaseDiscount, self).get_products()
            # code that excludes products that does not belong to self.categories
            return qs

    class CartItemPercentDiscount(SiteBaseDiscount, mixins.CartItemPercentDiscountMixin):
        pass

See :doc:`api_mixins`.

Example
-------

If client buy 5 or more items let the price for item be 10% lower.

Add this model::

    from discount.models import DiscountBase

    class BulkDiscount(DiscountBase):
        """
        Apply ``amount`` % of discount if there are at least ``num_items`` of
        product in cart.
        """
        amount = models.DecimalField(_('Amount'), max_digits=5, decimal_places=2)
        num_items = models.IntegerField(_('Minimum number of items'))

        def get_extra_cart_item_price_field(self, cart_item):
            if (cart_item.quantity >= self.num_items and
                self.is_eligible_product(cart_item.product, cart_item.cart)):
                amount = (self.amount/100) * cart_item.line_subtotal
                return (self.get_name(), amount,)

Given that you registered ``BulkDiscount`` with django admin,
site administrator would be able to set bulk discounts.

See this discount in action in :doc:`example_app`.
