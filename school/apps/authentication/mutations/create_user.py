from django.contrib.auth.models import User
import graphene
from graphql import GraphQLError
from django.core.validators import validate_email

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
        validate_email(email)
        password = validator.validate_password(password=kwargs.get('password'))
        user = User.objects.filter(email=email).first()
        if user:
            raise GraphQLError(
                AUTH_ERROR["email_in_use"].format(email))
        else:
            user = User(
                username=kwargs.get('username'),
                email=kwargs.get('email')
            )
            user.set_password(password)
            user.save()

            return CreateUser(
                user=user,
                message=AUTH_SUCCESS["created"]
            )
