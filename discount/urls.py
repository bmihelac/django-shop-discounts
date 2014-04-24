try:
    # django 1.6+
    from django.conf.urls import patterns,url
except ImportError:
    # django <1.6
    from django.conf.urls.defaults import patterns,url


from discount.views import CartDiscountCodeDeleteView, CartDiscountCodeCreateView


urlpatterns = patterns('',
    url(r'^discount_code/$', CartDiscountCodeCreateView.as_view(), 
        name='discount_cartdiscountcode_create'),
    url(r'^discount_code/delete/$', CartDiscountCodeDeleteView.as_view(), 
        name='discount_cartdiscountcode_delete'),
    )

