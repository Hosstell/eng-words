import graphene
from english.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.utils.crypto import get_random_string


class UserRegistrationType(graphene.InputObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()
    login = graphene.String()
    password = graphene.String()


class UserRegistration(graphene.Mutation):
    class Arguments:
        form = UserRegistrationType()

    result = graphene.Boolean()

    def mutate(self, info, form):
        if UserRegistration.check_existence(form):
            raise Exception('Такой пользователь существует')

        new_user = User.objects.create(
            first_name=form['first_name'],
            last_name=form['last_name'],
            email=form['email'],
            nickname=form['login']
        )
        new_user.set_password(form['password'])
        new_user.save()

        return UserRegistration(result=True)

    @classmethod
    def check_existence(cls, form):
        _filter = Q(email=form['email']) | Q(nickname=form['login'])
        return bool(User.objects.filter(_filter).count())


class UserLogin(graphene.Mutation):
    class Arguments:
        login = graphene.String(required=True)
        password = graphene.String(required=True)

    cookie = graphene.String()

    def mutate(self, info, login, password):
        user = authenticate(info.context, username=login, password=password)
        if user is not None:
            cookie = get_random_string(64)
            user.cookie = cookie
            user.save()
            return UserLogin(cookie=cookie)
        else:
            raise Exception('Неверный пароль')


class UserLogout(graphene.Mutation):
    result = graphene.Boolean()

    def mutate(self, info):
        try:
            user = info.context.user
            user.cookie = None
            user.save()
        except:
            pass
        return UserLogout(result=True)


class Mutation(graphene.ObjectType):
    user_registration = UserRegistration.Field()
    login = UserLogin.Field()
    logout = UserLogout.Field()
