from django.test import TestCase


"""
    Dado que temos visitante qualquer
    Quando acessa o endereço /inscrição/
    Então vê a página de inscrição
     e a página possui formulário
     e o formulário possui 4 campos
     e os campos são NOME, EMAIL, CPF e TELEFONE
     e o formulário possui um botão para se increver.
"""

class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def test_get(self):
        """ GET /inscricao/ must return status code 200 """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Must use subscriptions/subscription_form.html """
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')