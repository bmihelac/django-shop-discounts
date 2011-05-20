from django.contrib import admin

from discount.models import PercentDiscount
from discount.models import CartItemPercentDiscount


class PercentDiscountAdmin(admin.ModelAdmin):
    pass


class CartItemPercentDiscountAdmin(admin.ModelAdmin):
    pass


admin.site.register(PercentDiscount, PercentDiscountAdmin)
admin.site.register(CartItemPercentDiscount, CartItemPercentDiscountAdmin)


