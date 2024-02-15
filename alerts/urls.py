from rest_framework.routers import DefaultRouter
from alerts.views import AlertViewSet

router = DefaultRouter()
router.register("alerts", AlertViewSet, basename="alerts")
urlpatterns = router.urls