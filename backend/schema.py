import english.schema.query
import english.schema.mutation
import graphene

from graphene_django.debug import DjangoDebug


class Query(english.schema.query.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="_debug")


class Mutation(english.schema.mutation.Mutation, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="_debug")

schema = graphene.Schema(query=Query, mutation=Mutation)
