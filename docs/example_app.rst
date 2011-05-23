===================
Example application
===================

To test django-shop-discounts application and get a feeling how it works::

1. Make sure you have django-shop installed

2. Change directory to django-shop-discounts/example

3. Run::

   ./manage.py syncdb --all --noinput && ./manage.py migrate --fake && ./manage.py loaddata sample_data.json
   ./manage.py runserver

4. Username and password for admin are: admin:password
