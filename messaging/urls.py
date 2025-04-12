from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet

router = DefaultRouter()
router.register(r'', MessageViewSet, basename='mensagen')

urlpatterns = router.urls
