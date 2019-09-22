from graphene import List, Field
import graphene
from english.models import User, Word
from .types import UserType, WordType


class Query(graphene.ObjectType):
    all_users = List(UserType)
    get_words = List(WordType)
    get_current_user = Field(UserType)

    def resolve_all_users(self, info):
        return User.objects.all()

    def resolve_get_words(self, info):
        return Word.objects.all()

    def resolve_get_current_user(self, info):
        return info.context.user
