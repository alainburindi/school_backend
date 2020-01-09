import graphene
import graphql_jwt

from school.apps.authentication import schema as auth_schema
from school.apps.authentication.queries import auth_queries


class Query(auth_queries.Query, graphene.ObjectType):
    pass


class Mutation(
    auth_schema.Mutation, graphene.ObjectType
):
    token_auth = graphql_jwt.ObtainJSONWebToken().Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
