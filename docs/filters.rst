=======
Filters
=======

Filters are ``dict`` or ``callable`` types that, when registered with
discount class(es) influences which products are eligible for this
discount.

Filters as dict
---------------

Product queryset is filtered with field lookups defined in dict::

    filt = {'unit_price__gt': 10}
    # only products with unit_price > 10 are eligible
    DiscountBase.register_product_filter(filt)

Filters as callable
-------------------

Callable is called with two arguments:

* discount model

* product queryset

::
    def filt(discount, qs):
        # only product names as discount are eligible
        return(qs.filter(name=discount.name))

    DiscountBase.register_product_filter(filt)
