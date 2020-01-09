import json
from django.test import TestCase, Client
from school.apps.authentication.models import User


class TestConfig(TestCase):
    """
    Test configuration
    """
    @classmethod
    def setUpClass(cls):

        # We need to first run setUpClass function that we
        # inherited from TestCase.
        super(TestConfig, cls).setUpClass()

        # Set up test client for all test classes
        # that will inherit from this class.
        cls.client = Client()

    @classmethod
    def query(cls, query: str = None):
        # Method to run all queries and mutations for tests.
        body = dict()
        body['query'] = query
        response = cls.client.post(
            '/school/', json.dumps(body), content_type='application/json')
        json_response = json.loads(response.content.decode())
        return json_response

    # @classmethod
    # def query_with_token(cls, access_token, query: str = None):
    #     # Method to run queries and mutations using a logged in user
    #     # with an authentication token
    #     body = dict()
    #     body['query'] = query
    #     http_auth = 'JWT {}'.format(access_token)
    #     url = '/school/'
    #     content_type = 'application/json'

    #     response = cls.client.post(
    #         url,
    #         json.dumps(body),
    #         HTTP_AUTHORIZATION=http_auth,
    #         content_type=content_type)
    #     json_response = json.loads(response.content.decode())
    #     return json_response

    def setUp(self):
        self.default_user_data = {
            "email": "alain@school.com",
            "username": "Alainb", "password": "Password123"
        }

        self.default_user = self.register_user(self.default_user_data)

    def register_user(self, user):
        """
        register a new user
        """
        # email = user["email"]
        # mobile_number = user["mobile_number"]
        # password = user["password"]
        user = User.objects.create_user(**user)
        user.is_active = True
        user.save()
        return user
