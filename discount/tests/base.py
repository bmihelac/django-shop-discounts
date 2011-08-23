import uuid
from datetime import datetime
from decimal import Decimal

from django.test.testcases import TestCase
from django.conf import settings

from shop.models.productmodel import Product
from shop.models.cartmodel import Cart

from discount.models import (DiscountBase, PercentDiscount, 
        CartItemPercentDiscount, CartItemAbsoluteDiscount)


settings.SHOP_CART_MODIFIERS = ['discount.cart_modifiers.DiscountCartModifier']


class DiscountBaseTest(TestCase):

    def setUp(self):
        pass

    def test_01_active_discounts_with_is_active(self):
        discount = DiscountBase.objects.create(name='discount 1')
        self.assertIn(discount, DiscountBase.objects.active())

        discount.is_active = False
        discount.save()
        self.assertNotIn(discount, DiscountBase.objects.active())

    def test_02_active_discounts_with_period(self):
        discount = DiscountBase.objects.create(
                name='discount 1',
                valid_from='2009-01-01 12:00:00',
                valid_until='2009-01-01 15:00:00')
        self.assertNotIn(discount, DiscountBase.objects.active())

        at_datetime = datetime(2009, 1, 1, 13)
        self.assertIn(discount, DiscountBase.objects.active(at_datetime))

    def test_03_for_code(self):
        discount = DiscountBase.objects.create(name='discount 1')
        discount_with_code = DiscountBase.objects.create(name='discount 1',
                code='x123')

        self.assertIn(discount, DiscountBase.objects.active(code='x123'))
        self.assertIn(discount_with_code, DiscountBase.objects.active(code='x123'))

        self.assertNotIn(discount_with_code, DiscountBase.objects.active(code='YYY'))


class DiscountCartModifierTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
                name='test product',
                slug='test-product',
                unit_price=10,
                active=True)
        self.cart = Cart.objects.create()
        self.cart.add_product(self.product)

    def test_01_percent_discount(self):
        PercentDiscount.objects.create(name='dsc', amount="-10")
        self.cart.update({})
        self.assertEquals(self.cart.total_price, 9)
        self.assertEquals(len(self.cart.extra_price_fields), 1)
        self.assertEquals(self.cart.extra_price_fields[0][0], 'dsc')
        self.assertEquals(self.cart.extra_price_fields[0][1], Decimal("-1.00"))

    def test_02_with_valid_discount_code(self):
        PercentDiscount.objects.create(
                name='dsc', code='dsc10', amount="-10")
        self.cart.cartdiscountcode_set.create(code='dsc10')
        self.cart.update({})
        self.assertEquals(self.cart.total_price, 9)

    def test_03_without_valid_discount_code(self):
        PercentDiscount.objects.create(
                name='dsc', code='dsc10', amount="-10")
        self.cart.update({})
        self.assertEquals(self.cart.total_price, 10)


def create_product(**kwargs):
    data = {
            'name': 'test',
            'unit_price': Decimal("10.0"),
            'slug': str(uuid.uuid4()),
            }
    data.update(kwargs)
    return Product.objects.create(**data)


class DiscountProductFiltersTest(TestCase):

    def setUp(self):
        self.product_1 = create_product(unit_price=Decimal("10.0"))
        self.product_2 = create_product(unit_price=Decimal("20.0"))
        self.discount = DiscountBase.objects.create(name='discount 1')
        DiscountBase.product_filters = []

    def test_01_eligible_products_without_product_filters(self):
        self.assertIn(self.product_1, self.discount.eligible_products())
        self.assertIn(self.product_2, self.discount.eligible_products([]))

    def test_02_register_product_filter_with_dict(self):
        filt = {'unit_price__gt': 10}
        DiscountBase.register_product_filter(filt)
        self.assertNotIn(self.product_1, self.discount.eligible_products())
        self.assertIn(self.product_2, self.discount.eligible_products())

    def test_03_register_product_filter_with_callable(self):
        def filt(discount, qs):
            return(qs.filter(name=discount.name))

        DiscountBase.register_product_filter(filt)
        self.assertEquals(len(self.discount.eligible_products()), 0)

        product_discount = create_product(name=self.discount.name)
        self.assertIn(product_discount, self.discount.eligible_products())


class CartItemPercentDiscountTest(TestCase):

    def setUp(self):
        self.product_1 = create_product(unit_price=Decimal("10.0"))
        self.cart = Cart.objects.create()
        self.cart.add_product(self.product_1)
        self.discount = CartItemPercentDiscount.objects.create(name='dsc', 
                amount="-5")

    def test_01_cart_item_should_be_discounted(self):
        cart_item = self.cart.items.get(product=self.product_1)
        cart_item.update({})
        self.assertEquals(len(cart_item.extra_price_fields), 1)
        self.assertEquals(cart_item.extra_price_fields[0],
                ((unicode(self.discount), Decimal("-0.5"), )))


class CartItemAbsoluteDiscountTest(TestCase):

    def setUp(self):
        self.product_1 = create_product(unit_price=Decimal("10.0"))
        self.cart = Cart.objects.create()
        self.cart.add_product(self.product_1)
        self.discount = CartItemAbsoluteDiscount.objects.create(name='dsc', 
                amount="-1")

    def test_01_cart_item_should_be_discounted(self):
        cart_item = self.cart.items.get(product=self.product_1)
        cart_item.update({})
        self.assertEquals(len(cart_item.extra_price_fields), 1)
        self.assertEquals(cart_item.extra_price_fields[0],
                ((unicode(self.discount), Decimal("-1"), )))

