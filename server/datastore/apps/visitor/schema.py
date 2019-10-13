import graphene
from graphene_django import DjangoObjectType

from .models import Visitor

class VisitorType(DjangoObjectType):
    class Meta:
        model = Visitor

class Query_Visitor(graphene.ObjectType):
    visitors = graphene.List(VisitorType)

    def resolve_visitors(self,info,**kwargs):
        return Visitor.objects.all()

