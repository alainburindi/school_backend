import graphene

from .mutations.create_user import CreateUser
from .mutations.login import LoginUser


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    login = LoginUser.Field()
