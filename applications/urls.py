from .views import ApplicationModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ApplicationModelViewSet, basename='application')

urlpatterns = router.urls