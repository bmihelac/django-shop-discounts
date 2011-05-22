=======
Filters
=======

Example of implementing filtering products by category in DiscountBase:::

    def category_product_filter(discount, queryset):
        """
        Allow discount type to be filtered by category.
        """
        if not discount.categories.count():
            return queryset
        ids = [c.id for c in discount.categories.all()]
        return queryset.filter(models.Q( Book___categories__id__in=ids))

    DiscountBase.register_product_filter(category_product_filter)


    #add categories field to BulkDiscount
    BulkDiscount.add_to_class('categories', 
            models.ManyToManyField(Category, 
                verbose_name=_('Categories'),
                blank=True,
                null=True,
                help_text=_('Limit discount to selected categories')
                ))

This would allow editor to select to what categories of products all discount 
types applies.

This code is implemented in :doc:`example_app`.

