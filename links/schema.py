import graphene
from graphene_django import DjangoObjectType

from .models import Link


class LinkType(DjangoObjectType):
    class Meta:
        model = Link


class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    def resolve_links(self, info, **kwargs):
        return Link.objects.all()


class CreateLink(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()

    class Arguments:
        url = graphene.String()
        description = graphene.String()

    def mutate(self, info, url, description):
        link = Link(url=url, description=description)
        link.save()

        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description,
        )


class UpdateLink(graphene.Mutation):
    link = graphene.Field(LinkType)
    message = graphene.String()

    class Arguments:
        id = graphene.ID()
        description = graphene.String(required=False)
        url = graphene.String(required=False)

    def mutate(self, info, **kwargs):
        link = Link.objects.filter(id=kwargs.get('id')).first()
        link.url = kwargs.get('url') or link.url
        link.description = kwargs.get('description') or link.description
        link.save()

        return UpdateLink(link=link, message="updated correctly")


class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
    update_link = UpdateLink.Field()
