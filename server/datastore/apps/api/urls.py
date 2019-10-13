from rest_framework import routers
from django.urls import path,include
from apps.api.views import HelloView,UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = [
    path('users/hello/',HelloView.as_view(),name='hello'),
    path('',include(router.urls)),
]
