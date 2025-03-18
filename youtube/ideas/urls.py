from rest_framework import routers
from django.urls import path, include
from .views import IdeaViewSet, VoteViewSet

router = routers.DefaultRouter()
router.register(r'ideas', IdeaViewSet)
router.register(r'votes', VoteViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]