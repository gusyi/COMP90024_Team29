# ====================================
# COMP90024 Cluster and Cloud Computing - Assignment 2
# Group 29
# Hongwei Yin 901012
# Cheng Sun 900806
# Xinyi Xu 900966
# Yiran Yao 1144268
# Xiaotao Tan 1032950
# ====================================
from rest_framework import routers
from .api import TweetTestViewSet, TweetResultViewSet

router = routers.DefaultRouter()
router.register('api/tweets', TweetTestViewSet, 'tweets')
router.register('api/tweetsresult', TweetResultViewSet, 'tweetresult')

urlpatterns = router.urls
