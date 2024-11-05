from django.test import TestCase
from subscriptions import subscription_form


class SubscriptionFormTest(TestCase):
    def setUp(self):
        self.form = SubscriptionForm()

    def test_has_form(self):
        expected = ['name','cpf','email','phone']
        self.assertSequenceEqual(expected, list(self.form.fields))