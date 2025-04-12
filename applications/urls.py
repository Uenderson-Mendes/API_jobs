from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ApplicationViewSet

router = DefaultRouter()
router.register(r'', ApplicationViewSet, basename='Candidatura')

urlpatterns = router.urls
