from rest_framework import routers

from django.urls import path, include

from .views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comment')
router.register('posts', PostViewSet)
router.register('follow', FollowViewSet, basename='follow')
router.register('groups', GroupViewSet, basename='groups')

app_name = 'api'

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls))
]
