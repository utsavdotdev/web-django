from django.test import TestCase
from django.urls import reverse
from .utils import add

# Create your tests here.
class AddFunctionTestCase(TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)

class RegistrationFormPageTestCase(TestCase):
    def test_registration_contains_input_text(self):
        response = self.client.get(reverse('registration:form'));
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Name')
        self.assertContains(response,'Email')
        self.assertContains(response,'Password:')
