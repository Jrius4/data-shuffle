"""datastore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from rest_framework_jwt import views as jwt_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from django.views.decorators.csrf import csrf_exempt
from apps.api.views import UserViewSet
from apps.visitor.views import VisitorViewSet

from graphene_django.views import GraphQLView
from .schema import (schema_user,schema_visitor)

router = routers.DefaultRouter()
router.register(r'users',UserViewSet)
router.register('visitors',VisitorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api/',include('apps.api.urls')),
    path('api/',include('apps.visitor.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('api/login/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('graphql/users/', csrf_exempt(GraphQLView.as_view(schema=schema_user,graphiql=True))),
    path('graphql/visitors/', csrf_exempt(GraphQLView.as_view(schema=schema_visitor,graphiql=True))),
    path('gql/',csrf_exempt(GraphQLView.as_view(schema=schema_user,graphiql=True))),
]
