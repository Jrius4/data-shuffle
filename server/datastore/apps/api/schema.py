import graphene
from graphene_django import DjangoObjectType

from .models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User

class Query_User(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self,info,**kwargs):
        return User.objects.all()

# class Query_User(graphene.ObjectType):
#     users = graphene.List(UserType,first=graphene.Int())

#     def resolve_users(self,info,first,**kwargs):
#         return User.objects.all()[:first]

