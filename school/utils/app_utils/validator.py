import re
from graphql import GraphQLError
from django.contrib.auth.models import User
from django.db.models import Q

from school.utils.messages.authentication_response import AUTH_ERROR


class Validator:
    """
    All validations of fields within the system

    fields:
        new_password(str): password
    """

    def validate_password(self, password):
        """
        Validate password
        Args:
            password(str): the user's password
        returns:
            password(str): the sent password if it's correct
            error(GraphQLError): if the password is not valid
        """
        self.password = password.strip()
        regex = re.match('(?=.{8,100})(?=.*[A-Z])(?=.*[0-9])', self.password)
        if regex is None:
            raise GraphQLError(AUTH_ERROR["invalid_password"])
        return self.password

    def validate_user(self, **kwargs):
        """
        """
        email = kwargs.get("email")
        username = kwargs.get("username")
        users = User.objects.filter(Q(username=username) | Q(email=email))
        if email in [user.email for user in users]:
            raise GraphQLError(
                AUTH_ERROR["email_username_in_use"].format(key="email", value=email))
        elif username in [user.username for user in users]:
            raise GraphQLError(
                AUTH_ERROR["email_username_in_use"].format(key="username", value=username))


validator = Validator()
