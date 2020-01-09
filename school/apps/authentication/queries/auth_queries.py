import graphene
from graphql import GraphQLError

from ..types import UserType


class Query(graphene.ObjectType):
    me = graphene.Field(UserType)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('not logged in!')
        return user
