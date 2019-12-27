import graphene
import graphql_jwt

from school.apps.authentication import schema as auth_schema


# class Query(auth_schema.Query, graphene.ObjectType):
#     pass


class Mutation(
    auth_schema.Mutation, graphene.ObjectType
):
    token_auth = graphql_jwt.ObtainJSONWebToken().Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(mutation=Mutation)
