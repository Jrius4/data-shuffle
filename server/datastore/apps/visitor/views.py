from django.shortcuts import render
from .models import Visitor
from rest_framework.response import Response
from .serializers import VisitorProfileSerializer
from rest_framework import viewsets
from rest_framework.permissions import (AllowAny,IsAuthenticated)
from apps.api.permissions import IsLoggedInUserOrAdmin,IsAdminUser
from rest_framework.views import APIView

class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorProfileSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action =='patch':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes= [IsAdminUser]
        return [permission() for permission in permission_classes]
# Protected views
# Need a jwt token header to access this view
class VisitorHelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        content = {'message':'Hello, visitor!'}
        return Response(content)
