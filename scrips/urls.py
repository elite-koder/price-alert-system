from rest_framework.routers import DefaultRouter
from scrips.views import ScripViewSet

router = DefaultRouter()
router.register("scrips", ScripViewSet, basename="ticker-view-set")
urlpatterns = router.urls