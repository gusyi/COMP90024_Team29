from rest_framework import routers
from .api import TweetTestViewSet, TweetResultViewSet

router = routers.DefaultRouter()
router.register('api/tweets', TweetTestViewSet, 'tweets')
router.register('api/tweetsresult', TweetResultViewSet, 'tweetresult')

urlpatterns = router.urls