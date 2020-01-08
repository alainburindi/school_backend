import graphene
from django.db.models import Q
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from graphql_jwt.utils import jwt_encode, jwt_payload


from ..types import UserType
from school.utils.messages.authentication_response import (
    AUTH_SUCCESS
)

from school.utils.app_utils.responses import error
from ..models import User


class LoginUser(graphene.Mutation):
    message = graphene.String()
    token = graphene.String()
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String()
        email = graphene.String()
        password = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        email = kwargs.get('email')
        username = kwargs.get('username')
        password = kwargs.get('password')
        if email is None and username is None:
            error.invalid_credentials()
        try:
            user = User.objects.get(
                Q(username=username) | Q(email=email)
            )
            auth_user = check_password(password, user.password)
            if not auth_user:
                error.invalid_credentials()
            payload = jwt_payload(user)
            token = jwt_encode(payload)
            return LoginUser(
                message=AUTH_SUCCESS["success_login"],
                token=token,
                user=user
            )
        except ObjectDoesNotExist:
            error.invalid_credentials()
