from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscriptionPostValid(TestCase):
    def setUp(self):
        data = dict(name='John Mayer', cpf='12345678901', email='john@mayer.com', phone='21-99999-9999')
        self.resp = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'john@mayer.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['John Mayer', '12345678901', 'john@mayer.com', '21-99999-9999']

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
