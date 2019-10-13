from django.urls import path,include
from apps.visitor.views import VisitorHelloView,VisitorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'visitors', VisitorViewSet)
urlpatterns = [
    path('visitors/hello',VisitorHelloView.as_view(),name='hello'),
    path('',include(router.urls)),
]
