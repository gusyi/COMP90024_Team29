from rest_framework import routers
from .api import TweetViewSet

router = routers.DefaultRouter()
router.register('api/twitter', TweetViewSet, 'twitter')

urlpatterns = router.urls