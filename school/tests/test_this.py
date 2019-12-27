from school.tests.base_config import TestConfig
from school.tests.test_fixtures.authentication import (
    create_user
)
from school.utils.messages.authentication_response import (
    AUTH_SUCCESS, AUTH_ERROR
)


class TestI(TestConfig):

    def setUp(self):
        super(TestI, self).setUp()
        self.user = {"email": "alain@school.com",
                     "username": "Alainb", "password": "Password123"}

    def test_good(self):
        self.setUp()
        response = self.query(create_user.format(**self.user))
        self.assertEqual(AUTH_SUCCESS["created"],
                         response["data"]["createUser"]["message"])
        self.assertDictContainsSubset(
            response["data"]["createUser"]["user"], self.user)
        # used email
        response = self.query(create_user.format(**self.user))
        self.assertEqual(AUTH_ERROR["email_in_use"].format(self.user["email"]),
                         response["errors"][0]["message"])

    def test_invalid_password(self):
        self.user["password"] = "invalid"
        response = self.query(create_user.format(**self.user))
        self.assertEqual(AUTH_ERROR["invalid_password"],
                         response["errors"][0]["message"])
