from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetUp(APITestCase):
    """All the tests will inherit this class so that they can have APITestCase 
    class methods since this class is inherited by it and also the methods defined in this class.
    """

    def setUp(self):
        """Setup will provide variables to all the tests and must be called at the start of the test."""
        self.register_url = reverse(
            'register')  # reverse has names of the urls
        self.login_url = reverse('token_obtain_pair')
        self.getNewAccessToken_url = reverse('token_refresh')
        self.getUserData_url = reverse('user')
        self.testAuthenticated_url = reverse('test')
        self.logout_url = reverse('logout')
        self.user_data = {
            'email': 'test@test.com',
            'username': 'test',
            'first_name': 'firstname',
            'last_name': 'lastname',
            'password': 'test123'
        }
        return super().setUp()

    def tearDown(self):
        """Should be called at the end of the test, destroys test and related things."""
        return super().tearDown()
