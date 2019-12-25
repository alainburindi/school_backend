import re
from graphql import GraphQLError

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


validator = Validator()
