import graphene
from graphql import GraphQLError
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from graphql_jwt.utils import jwt_encode, jwt_payload


from ..types import UserType


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
            raise GraphQLError("Invalid login credentials")
        try:
            user = User.objects.get(
                Q(username=username) | Q(email=email)
            )
            auth_user = check_password(password, user.password)
            if not auth_user:
                raise GraphQLError("Invalid login credentials")
            payload = jwt_payload(user)
            token = jwt_encode(payload)
            return LoginUser(
                message="login successful",
                token=token,
                user=user
            )
        except ObjectDoesNotExist:
            raise GraphQLError("Invalid login credentials")
