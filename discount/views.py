from django.views.generic.edit import CreateView
from django.views.generic import View
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy

from shop.util.cart import get_or_create_cart

from models import CartDiscountCode


# TODO: handle ajax


class CartDiscountCodeCreateView(CreateView):
    model = CartDiscountCode
    success_url = reverse_lazy('checkout_selection')

    def get_form_kwargs(self):
        kwargs = super(CartDiscountCodeCreateView, self).get_form_kwargs()
        cart = get_or_create_cart(self.request, True)
        instance = CartDiscountCode(cart=cart)
        kwargs.update({'instance': instance})
        return kwargs


class CartDiscountCodeDeleteView(View):
    success_url = reverse_lazy('checkout_selection')

    def get_success_url(self):
        return self.success_url

    def post(self, *args, **kwargs):
        cart = get_or_create_cart(self.request)
        cart.cartdiscountcode_set.all().delete()
        return redirect(self.get_success_url())
