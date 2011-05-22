============
Installation
============

1. Add `discount` to INSTALLED_APPS::

    INSTALLED_APPS = (
        'shop', # The django SHOP application
        'discount',
    )

2. Add `DiscountCartModifier` to `SHOP_CART_MODIFIERS`::

    SHOP_CART_MODIFIERS = [
            'discount.cart_modifiers.DiscountCartModifier',
            ]

3. Include urls:::

    urlpatterns = patterns('',
        (r'^discount/', include('discount.urls')),
    )
