from rest_framework import routers
from .api import ProblemViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register("api/problem", ProblemViewSet, "problem")
router.register("api/message", MessageViewSet, "message")

urlpatterns = router.urls