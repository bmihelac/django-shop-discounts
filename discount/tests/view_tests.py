from django.test.testcases import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import AnonymousUser

from discount.models import DiscountBase
from discount.views import (
        CartDiscountCodeCreateView,
        )


class CartDiscountCodeCreateViewTest(TestCase):

    def setUp(self):
        self.discount = DiscountBase.objects.create(name='discount 1',
                code='x123')
        self.factory = RequestFactory()

    def test_code_validation(self):
        request = self.factory.post('', {'code': 'invalid code'})
        request.user = AnonymousUser()
        request.session = {}
        response = CartDiscountCodeCreateView.as_view()(request)
        self.assertEquals(response.status_code, 200)
        self.assertIn('code', response.context_data['form'].errors)
