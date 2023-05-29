from Users.views import RegisterView
from Posts.views import PostCreateView, PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users/sign-in', RegisterView, basename="Register_View")
router.register('new-post', PostCreateView, basename="PostCreate_View")
router.register('view-post', PostViewSet, basename="Post_View")
urlpatterns=router.urls
