from django.conf.urls.defaults import url, patterns

from discount.views import CartDiscountCodeDeleteView, CartDiscountCodeCreateView


urlpatterns = patterns('',
    url(r'^discount_code/$', CartDiscountCodeCreateView.as_view(), 
        name='discount_cartdiscountcode_create'),
    url(r'^discount_code/delete/$', CartDiscountCodeDeleteView.as_view(), 
        name='discount_cartdiscountcode_delete'),
    )

