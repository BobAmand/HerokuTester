from django.test import TestCase
from django.core.urlresolvers import resolve
from .views import registration_page

# Create your tests here.


class RegisterPageTestCase(TestCase):

    def test_register_url_resoves_to_registration_page(self):
        found_registration_page = resolve('/register')
        self.assertEqual(found_registration_page, registration_page)
