from graphene_django.types import DjangoObjectType
from english.models import User, Word


class UserType(DjangoObjectType):
    class Meta:
        model = User


class WordType(DjangoObjectType):
    class Meta:
        model = Word
