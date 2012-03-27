===============
Getting started
===============

Configuration
-------------

1. Add `discount` to INSTALLED_APPS::

    INSTALLED_APPS = (
        'shop', # The django SHOP application
        'discount',
    )

2. Add `DiscountCartModifier` to `SHOP_CART_MODIFIERS`::

    SHOP_CART_MODIFIERS = [
            'discount.cart_modifiers.DiscountCartModifier',
            ]

``DiscountCartModifier`` is implemented as `django-shop` cart modifier.
It will be called on every `Cart` update call.

``DiscountCartModifier`` loops through active discounts adding extra cart 
or extra cart item field when given discount is eligible:

Active discounts are discounts with set ``active`` flag and within date range 
specified with Valid from - Valid to.

If ``code`` for the discount is set, user have to enter this `code` to
activate discount.

3. Include django-shop-discount urls::

    urlpatterns = patterns('',
        (r'^discount/', include('discount.urls')),
    )

This will include views for entering and removing discount code.

Quick start
-----------

django-shop-discount includes few bundled discount types.

To use them, add ``discount.default_discounts`` app to `INSTALLED_APPS`.

Next steps
----------

* :doc:`Custom discounts<extending_discounts>`

* :doc:`Discount filters<filters>`
