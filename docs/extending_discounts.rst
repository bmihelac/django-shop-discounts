=========================
Extending discounts types
=========================

Adding your own discount types is easy.

It is achived with subclassing ``discount.models.DiscountBase``
class and implementing ``process_cart_item`` or ``process_cart`` methods.

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

        def process_cart_item(self, cart_item):
            if (cart_item.quantity >= self.num_items and
                self.is_eligible_product(cart_item.product, cart_item.cart)):
                amount = (self.amount/100) * cart_item.line_subtotal
                to_append = (self.get_name(), amount)
                cart_item.extra_price_fields.append(to_append)

Given that you registered ``BulkDiscount`` to django admin, editor would be able
to set bulk discounts.

This code is implemented in :doc:`example_app`.
