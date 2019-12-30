from school.tests.base_config import TestConfig
from school.tests.test_fixtures.authentication import (
    create_user, login_user, login_empty_email_and_username
)
from school.utils.messages.authentication_response import (
    AUTH_SUCCESS, AUTH_ERROR
)


class TestAuth(TestConfig):

    def setUp(self):
        super(TestAuth, self).setUp()
        self.user = {"email": "alainsecond@school.com",
                     "username": "Alainsecond", "password": "Password123"}

    def test_signup(self):
        response = self.query(create_user.format(**self.user))
        self.assertEqual(AUTH_SUCCESS["created"],
                         response["data"]["createUser"]["message"])
        self.assertDictContainsSubset(
            response["data"]["createUser"]["user"], self.user)
        # used email
        response = self.query(create_user.format(**self.user))
        self.assertEqual(AUTH_ERROR["email_username_in_use"].format(
            key="email", value=self.user["email"]),
            response["errors"][0]["message"]
        )

    def test_duplicate_username(self):
        self.default_user_data['email'] = "unusedemail@school.com"
        response = self.query(create_user.format(**self.default_user_data))
        self.assertEqual(AUTH_ERROR["email_username_in_use"].format(
            key="username", value=self.default_user_data["username"]),
            response["errors"][0]["message"]
        )

    def test_invalid_password(self):
        self.user["password"] = "invalid"
        response = self.query(create_user.format(**self.user))
        self.assertEqual(AUTH_ERROR["invalid_password"],
                         response["errors"][0]["message"])

    def test_login(self):
        response = self.query(login_user.format(**self.default_user_data))
        self.assertEqual(AUTH_SUCCESS["success_login"],
                         response["data"]["login"]["message"])

    def test_empty_email_and_username(self):
        response = self.query(login_empty_email_and_username)
        self.assertEqual(AUTH_ERROR["invalid_credentials"],
                         response["errors"][0]["message"])

    def test_login_unexisting_user(self):
        response = self.query(login_user.format(**self.user))
        self.assertEqual(AUTH_ERROR["invalid_credentials"],
                         response["errors"][0]["message"])

    def test_login_invalid_password(self):
        self.default_user_data["password"] = "wrong"
        response = self.query(login_user.format(**self.default_user_data))
        self.assertEqual(AUTH_ERROR["invalid_credentials"],
                         response["errors"][0]["message"])
