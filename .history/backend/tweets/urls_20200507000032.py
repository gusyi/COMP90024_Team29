from rest_framework import routers
from .api import TweetTestViewSet

router = routers.DefaultRouter()
router.register('api/tweets', TweetTestViewSet, 'tweets')

urlpatterns = router.urls