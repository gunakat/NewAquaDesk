from django.db import router
from django.urls import path
from django.urls.conf import include
from .views import (LifeformSerializerViewSet,CountsessionSerializerViewSet,
                    TankSerializerAPIView,TankSerializerAPI,CountsessionSerializerAPI,
                    TankModelViewSet,CountsessionModelViewSet)
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
# from . import views

# urlpatterns = [
#     path('lifeformapi',views.LifeformSerializerViewSet, name='lifeformapi'),
#     path('countsessionapi',views.CountsessionSerializerViewSet, name='Countsessionapi'),
#     path('tankapi',views.TankSerializerViewSet, name='tankapi'),
# ]
# router = DefaultRouter()
# router.register('lifeform',LifeformSerializerViewSet)
router = DefaultRouter(trailing_slash=False)
router.register(r'tank', TankModelViewSet, basename='tank')


# urlpatterns = router1.urls

# router2 = DefaultRouter(trailing_slash=False)
router.register(r'countsession', CountsessionModelViewSet, basename='countsession')


# urlpatterns = router2.urls

urlpatterns = [
    # path('lifeform/',include(router.urls)),
    path('lifeformapi',LifeformSerializerViewSet, name='lifeformapi'),
    path('countsessionapi',CountsessionSerializerViewSet, name='Countsessionapi'),
    path('tankapi',TankSerializerAPIView.as_view(), name='tankapi'),
    path('tankapi1',TankSerializerAPI, name='tankapi1'),
    path('countsessionapi1',CountsessionSerializerAPI, name='countsessionapi1'),
    # router2.urls,
    path('', include(router.urls)),
]