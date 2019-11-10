import graphene

import links.schema
import authentication.schema


class Query(links.schema.Query, graphene.ObjectType):
    pass


class Mutation(authentication.schema.Mutation, links.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
