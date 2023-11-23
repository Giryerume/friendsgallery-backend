from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from user_profile.views import UserProfileViewSet
from photos.views import ApprovedPhotosViewSet, PhotoViewSet
from comments.views import CommentViewSet
from likes.views import LikeViewSet
from approve.views import ApproveViewSet
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView
from api.views import CustomTokenObtainPairView

router=DefaultRouter()

urlpatterns=[
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/blacklist/', TokenBlacklistView.as_view(), name="token_blacklist")
]

router.register(r'users', UserViewSet, basename='users')
router.register(r'user_profiles', UserProfileViewSet)
router.register(r'approved_photos', ApprovedPhotosViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'approve', ApproveViewSet)

urlpatterns=urlpatterns+router.urls
