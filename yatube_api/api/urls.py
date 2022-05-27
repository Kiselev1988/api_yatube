from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from api.views import CommentViewSet, GroupViewSet, PostViewSet


router = DefaultRouter()

router.register(r'v1/posts', PostViewSet, basename='post')
router.register(r'v1/groups', GroupViewSet, basename='group')
router.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment',
)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
