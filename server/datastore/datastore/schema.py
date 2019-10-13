import graphene

from apps.api.schema import Query_User
from apps.visitor.schema import Query_Visitor



class QueryUser(Query_User, graphene.ObjectType):
    pass


class QueryVisitor(Query_Visitor, graphene.ObjectType):
    pass


schema_user = graphene.Schema(query=QueryUser)
schema_visitor = graphene.Schema(query=QueryVisitor)