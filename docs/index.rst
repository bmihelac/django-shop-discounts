============================
Discount app for django-shop
============================

django-shop-discounts aims to be configurable and extendible discount
app for Django-shop.

Features:

* multiple discount types

* define date ranges when discount is valid

* discount codes (that need to be entered by user for discount to be valid)

* registering filters allow narrowing products discounts may apply to
  (for example by site, product category, color, etc)

django-shop-discounts is currently considered alpha version.

User Guide
----------

.. toctree::
   :maxdepth: 2

   installation
   getting_started
   extending_discounts
   filters
   example_app
   todo
   contributing
   changelog

API documentation
-----------------

.. toctree::
   :maxdepth: 2

   api_models
   api_managers
   api_views
   api_mixins
   api_default_discounts
