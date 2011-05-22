=====
Usage
=====

``DiscountCartModifier`` is django-shop cart modifier. It would be called on 
every cart update call.

``DiscountCartModifier`` loop through active discounts for cart and for for
discounts with eligible products in cart it may add:

* extra price field for whole cart,

* extra price field for individual cart items

Active discounts
----------------

Active discounts are discounts with ``active`` flag and within date range 
specified with Valid from - Valid to.

If ``code`` for the discount is set, for dicount to be active Cart object 
should have associated CartDiscountCode with same code.

Eligible products
-----------------

Eligible products for discounts are selected based on filters.

See :doc:`filters`.
