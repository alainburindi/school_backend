from django.contrib.auth.models import User
import graphene
from django.core.validators import validate_email

from school.utils.app_utils.validator import validator
from school.utils.messages.authentication_response import (
    AUTH_SUCCESS
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
