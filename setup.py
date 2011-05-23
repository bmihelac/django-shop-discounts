from setuptools import setup, find_packages
import os


VERSION = __import__("discount").__version__

setup(
    name="django-shop-discounts",
    description="configurable and extendible discount app for Django-shop",
    long_description=open(os.path.join(os.path.dirname(__file__), 
        'README.rst')).read(),
    version=VERSION,
    author="Bojan Mihelac",
    author_email="bmihelac@mihelac.org",
    url="https://github.com/bmihelac/django-shop-discounts",
    install_requires=[
        'django-shop',
        ],
    packages=find_packages(exclude=["example", "example.*"]),
)

