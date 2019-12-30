from django.contrib.auth.models import User
import graphene
from graphql import GraphQLError
from django.core.validators import validate_email
from django.db.models import Q

from school.utils.app_utils.validator import validator
from school.utils.messages.authentication_response import (
    AUTH_SUCCESS, AUTH_ERROR
)
from school.apps.authentication.types import UserType


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    message = graphene.String()

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        email = kwargs.get('email')
        username = kwargs.get('username')
        validate_email(email)
        password = validator.validate_password(password=kwargs.get('password'))
        # user = User.objects.get(Q(username=username) | Q(email=email))
        # if user:
        #     raise GraphQLError(
        #         AUTH_ERROR["email_username_in_use"].format(key="email", value=email))
        # # user = User.objects.filter(username=username).first()
        # if user:
        #     raise GraphQLError(
        #         AUTH_ERROR["email_username_in_use"].format(key="username", value=username))
        validator.validate_user(**kwargs)
        user = User(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()

        return CreateUser(
            user=user,
            message=AUTH_SUCCESS["created"]
        )
