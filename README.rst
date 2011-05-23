=====================
django-shop-discounts
=====================

django-shop-discounts let's you say:

* 5% percents discount for all products when code "Summer2011" is used

* 10% percent discount if client buy 5 or more books in fiction

* 35% percent discount on all fiction books during holidays

* or whatever you want

This repository hosts django-shop-discounts application which 
aims to bring configurable and extendible discount app for Django-shop.

Current features:

* multiple discount types

* define date ranges when discount is valid

* discount codes (that need to be entered by user for discount to be valid)

* defining filters to allow selecting products to which discounts may apply
  (by product category, color, whatever)

The source code for django-shop-discounts can be found and contributed to on 
`github.com/bmihelac/django-shop-discounts`_. There you can also file tickets.

django-shop-discounts is currently considered alpha version.

Example application
-------------------

To test django-shop-discounts application and get a feeling how it works::

1. Make sure you have django-shop installed

2. Change directory to django-shop-discounts/example

3. Run::

   ./manage.py syncdb --all --noinput && ./manage.py migrate --fake && ./manage.py loaddata sample_data.json
   ./manage.py runserver

4. Username and password for admin are: admin:password

