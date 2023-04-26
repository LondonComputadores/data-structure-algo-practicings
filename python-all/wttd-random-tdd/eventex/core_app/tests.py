from django.test import TestCase


# Chapter: Desenvolvimento Ágil

# Aula: O resgate do código não testado

# V2

class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """ Get must return status code 200 """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Must use index.html """
        self.assertTemplateUsed(self.response, 'index.html')



# V1

# class HomeTest(TestCase):
#     def test_get(self):
#         """ Get must return status code 200 """
#         response = self.client.get('/')
#         #self.assertEqual(404, response.status_code) # Must fail test
#         self.assertEqual(200, response.status_code)  # Must pass test

#     def test_template(self):
#         """ Must use index.html """
#         response = self.client.get('/')
#         self.assertTemplateUsed(response, 'index.html')
 