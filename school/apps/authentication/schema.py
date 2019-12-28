import graphene

from .mutations.create_user import CreateUser
from .mutations.login import LoginUser


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    login = LoginUser.Field()

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
