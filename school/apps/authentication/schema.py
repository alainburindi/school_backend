from django.contrib.auth.models import User
import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.core.validators import validate_email

from school.utils.app_utils.validator import validator
from school.utils.messages.authentication_response import (
    AUTH_SUCCESS, AUTH_ERROR
)


class UserType(DjangoObjectType):
    class Meta:
        model = User


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


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


# class Query(graphene.ObjectType):
#     users = graphene.List(UserType)
#     me = graphene.Field(UserType)

#     def resolve_users(self, info):
#         return User.objects.all()

#     def resolve_me(self, info):
#         user = info.context.user
#         if user.is_anonymous:
#             raise GraphQLError('not logged in!')

#         return user
