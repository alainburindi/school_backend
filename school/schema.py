import graphene
import graphql_jwt

import links.schema
import authentication.schema


class Query(authentication.schema.Query, links.schema.Query, graphene.ObjectType):
    pass


class Mutation(authentication.schema.Mutation, links.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken().Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
