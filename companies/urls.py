from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet

router = DefaultRouter()
router.register(r'', CompanyViewSet, basename='Empresa')

urlpatterns = router.urls
