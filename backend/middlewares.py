from django.core.exceptions import PermissionDenied
from graphene.utils.str_converters import to_snake_case
from english.models import User

permission_denied_string = '401::Необходимо осуществить вход в систему'


class AuthorizationMiddleware(object):
    def resolve(self, next, root, info, **args):
        try:
            cookie = info.context.COOKIES['custom-cookie']
            user = User.objects.get(cookie=cookie)
            info.context.user = user
        except:
            info.context.user = None
        # field_name = to_snake_case(info.field_name)
        # if hasattr(info.parent_type, 'graphene_type'):
        #     field = getattr(info.parent_type.graphene_type, field_name, None)
        #     if field:
        #         allow_unauthorized = getattr(field, 'allow_unauthorized', False)
        #         if (not allow_unauthorized and info.context.user.is_authenticated) or allow_unauthorized:
        #             return next(root, info, **args)
        #         else:
        #             raise PermissionDenied(permission_denied_string)
        return next(root, info, **args)
